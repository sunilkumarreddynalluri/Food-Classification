import json
import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
r.flushdb()  # Clears old, wrong keys

with open('food_nutrition.json', "r") as file:
    data = json.load(file)

    # If your JSON has a "food_classes" wrapper, we skip it to get to the items
    items = data.get("food_classes", data)

    for food_name, nutrition in items.items():
        # Standardize: "Chicken Curry" -> "chicken_curry"
        standard_key = food_name.lower().replace(" ", "_").strip()
        r.set(standard_key, json.dumps(nutrition))
        print(f"Stored: {standard_key}")