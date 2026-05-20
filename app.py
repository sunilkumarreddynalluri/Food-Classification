import os
import json
import io

import redis
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import tensorflow as tf

# ─────────────────────────────────────────
#  App Setup
# ─────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
CORS(app)

# Redis connection
r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

# ─────────────────────────────────────────
#  Labels  (must match training indices)
# ─────────────────────────────────────────
LABELS = [
    "butter_naan", "pav_bhaji", "Sandwich", "chicken_curry", "Hot Dog",
    "cheesecake", "sushi", "chai", "burger", "ice_cream", "kadai_paneer",
    "Baked Potato", "chapati", "masala_dosa", "dal_makhani", "Donut",
    "jalebi", "fried_rice", "chole_bhature", "kulfi", "kaathi_rolls",
    "dhokla", "Fries", "omelette", "pakode", "momos", "paani_puri",
    "samosa", "Taco", "idli", "Taquito", "Crispy Chicken", "pizza", "apple_pie",
]
NUM_CLASSES = len(LABELS)  # 34

# ─────────────────────────────────────────
#  Validation metrics per model
#  Replace these with your actual eval numbers.
# ─────────────────────────────────────────
MODEL_METRICS = {
    "custom_cnn": {"accuracy": 0.494, "precision": 0.512, "f1": 0.487},
    "vgg16":      {"accuracy": 0.673, "precision": 0.689, "f1": 0.671},
    "resnet50":   {"accuracy": 0.721, "precision": 0.735, "f1": 0.724},
}

# In-memory model cache
_models: dict = {}

# ─────────────────────────────────────────
#  Model Builders
# ─────────────────────────────────────────

def build_custom_cnn(input_shape=(256, 256, 3), num_classes=NUM_CLASSES):
    inputs = tf.keras.Input(shape=input_shape)
    x = inputs
    for filters in [32, 64, 128, 256, 512]:
        x = tf.keras.layers.Conv2D(filters, (3, 3), activation="relu", padding="same")(x)
        x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Flatten()(x)
    for units in [1024, 512, 256, 128, 64]:
        x = tf.keras.layers.Dense(units, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(inputs, outputs)


def build_vgg16(num_classes=NUM_CLASSES):
    base = tf.keras.applications.VGG16(
        weights=None, include_top=False, input_shape=(224, 224, 3)
    )
    x = tf.keras.layers.Flatten()(base.output)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(base.input, outputs)


def build_resnet50(num_classes=NUM_CLASSES):
    base = tf.keras.applications.ResNet50(
        weights=None, include_top=False, input_shape=(224, 224, 3)
    )
    x = tf.keras.layers.GlobalAveragePooling2D()(base.output)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(base.input, outputs)

# ─────────────────────────────────────────
#  Helper: Load Model (cached)
# ─────────────────────────────────────────

WEIGHT_FILES = {
    "custom_cnn": "food_classification_weights.weights.h5",
    "vgg16":      "vgg16_food_classification_weights.weights.h5",
    "resnet50":   "resnet50_food_classification_weights.weights.h5",
}

BUILDERS = {
    "custom_cnn": build_custom_cnn,
    "vgg16":      build_vgg16,
    "resnet50":   build_resnet50,
}


def load_model(model_name: str):
    if model_name in _models:
        return _models[model_name]

    weight_path = os.path.join(BASE_DIR, WEIGHT_FILES[model_name])
    model = BUILDERS[model_name]()

    try:
        model.load_weights(weight_path)
    except Exception:
        model.load_weights(weight_path, skip_mismatch=True)

    _models[model_name] = model
    return model

# ─────────────────────────────────────────
#  Helper: Preprocess Image
# ─────────────────────────────────────────

INPUT_SIZES = {
    "custom_cnn": (256, 256),
    "vgg16":      (224, 224),
    "resnet50":   (224, 224),
}


def preprocess(image_bytes: bytes, model_name: str) -> np.ndarray:
    size = INPUT_SIZES.get(model_name, (256, 256))
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize(size)
    img_array = np.array(img, dtype=np.float32)
    img_batch = np.expand_dims(img_array, axis=0)

    if model_name == "vgg16":
        from tensorflow.keras.applications.vgg16 import preprocess_input
        return preprocess_input(img_batch)
    if model_name == "resnet50":
        from tensorflow.keras.applications.resnet50 import preprocess_input
        return preprocess_input(img_batch)
    return img_batch / 255.0

# ─────────────────────────────────────────
#  Helper: Nutrition from Redis
# ─────────────────────────────────────────

def get_nutrition(food_name: str) -> dict | None:
    """Look up nutrition data stored in Redis as JSON strings."""
    try:
        key = food_name.lower().replace(" ", "_").strip()
        raw = r.get(key)
        if raw:
            data = json.loads(raw)
            return {
                "calories":      data.get("calories", 0),
                "protein":       data.get("protein", 0),
                "carbohydrates": data.get("carbohydrates", 0),
                "fats":          data.get("fats", 0),
                "fiber":         data.get("fiber", 0),
            }
    except Exception as exc:
        print(f"[Redis] Lookup error for '{food_name}': {exc}")
    return None

# ─────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects multipart/form-data with:
      - image : food image file
      - model : 'custom_cnn' | 'vgg16' | 'resnet50'

    Returns JSON:
      predicted_label, confidence, top5, model_used,
      nutrition, metrics (accuracy / precision / f1)
    """
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        model_name = (
            request.form.get("model", "custom_cnn")
            .strip().lower().replace(" ", "_")
        )
        if model_name not in BUILDERS:
            return jsonify({"error": f"Unknown model: {model_name}"}), 400

        image_bytes = request.files["image"].read()
        model       = load_model(model_name)
        processed   = preprocess(image_bytes, model_name)
        preds       = model.predict(processed, verbose=0)[0]

        top_idx = int(np.argmax(preds))
        label   = LABELS[top_idx]

        # Top-5 predictions
        top5_indices = np.argsort(preds)[::-1][:5]
        top5 = [
            {"label": LABELS[i], "confidence": float(preds[i])}
            for i in top5_indices
        ]

        # Model validation metrics
        metrics = MODEL_METRICS.get(model_name, {})

        return jsonify({
            "predicted_label": label,
            "confidence":      round(float(preds[top_idx]) * 100, 2),
            "top5":            top5,
            "model_used":      model_name,
            "nutrition":       get_nutrition(label),
            "metrics": {
                "accuracy":  round(metrics.get("accuracy",  0) * 100, 1),
                "precision": round(metrics.get("precision", 0) * 100, 1),
                "f1":        round(metrics.get("f1",        0) * 100, 1),
            },
        })

    except Exception as exc:
        print(f"[ERROR] {exc}")
        return jsonify({"error": str(exc)}), 500


@app.route("/metrics/<model_name>", methods=["GET"])
def get_metrics(model_name: str):
    """
    Optional standalone endpoint to get validation metrics for a model.
    GET /metrics/custom_cnn  →  { accuracy, precision, f1 }
    """
    model_name = model_name.strip().lower().replace(" ", "_")
    if model_name not in MODEL_METRICS:
        return jsonify({"error": f"Unknown model: {model_name}"}), 404

    m = MODEL_METRICS[model_name]
    return jsonify({
        "model":     model_name,
        "accuracy":  round(m["accuracy"]  * 100, 1),
        "precision": round(m["precision"] * 100, 1),
        "f1":        round(m["f1"]        * 100, 1),
    })


# ─────────────────────────────────────────
#  Entry Point
# ─────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)