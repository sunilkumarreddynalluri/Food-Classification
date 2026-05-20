# Food-Classification
```html id="x82jfd"
<h1 align="center">🍔 Food Classification Using Deep Learning</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-Deep_Learning-orange?style=for-the-badge&logo=tensorflow">
  <img src="https://img.shields.io/badge/Keras-CNN-red?style=for-the-badge&logo=keras">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Accuracy-97%25-success?style=for-the-badge">
</p>

<hr>

<h2>📌 ABSTRACT</h2>

<p>
Food Classification Using Deep Learning is an AI-powered Computer Vision project developed to automatically identify and classify food categories from images using Deep Learning techniques.
</p>

<p>
The system was built using multiple deep learning architectures including:
</p>

<ul>
<li>Custom CNN</li>
<li>VGG16 Transfer Learning</li>
<li>ResNet50 Transfer Learning</li>
</ul>

<p>
The project performs image preprocessing, feature extraction, data augmentation, model training, and prediction using TensorFlow and Keras.
</p>

<p>
Among all models, ResNet50 achieved the highest accuracy with excellent classification performance.
</p>

<hr>

<h2>📊 DATASET OVERVIEW</h2>

<table border="1" cellpadding="10">

<tr>
<th>Attribute</th>
<th>Details</th>
</tr>

<tr>
<td>Total Classes</td>
<td>Multiple Food Categories</td>
</tr>

<tr>
<td>Image Type</td>
<td>RGB Food Images</td>
</tr>

<tr>
<td>Task</td>
<td>Multi-Class Image Classification</td>
</tr>

<tr>
<td>Framework</td>
<td>TensorFlow & Keras</td>
</tr>

</table>

<hr>

<h2>🍕 FOOD CATEGORIES</h2>

<table border="1" cellpadding="10">

<tr>
<th>Indian Foods</th>
<th>Fast Foods</th>
<th>Asian Foods</th>
</tr>

<tr>

<td>

<ul>
<li>Butter Naan</li>
<li>Pav Bhaji</li>
<li>Masala Dosa</li>
<li>Samosa</li>
<li>Chole Bhature</li>
<li>Idli</li>
<li>Jalebi</li>
<li>Chai</li>
</ul>

</td>

<td>

<ul>
<li>Burger</li>
<li>Pizza</li>
<li>Sandwich</li>
<li>Fries</li>
<li>Donut</li>
<li>Cheesecake</li>
<li>Taco</li>
<li>Crispy Chicken</li>
</ul>

</td>

<td>

<ul>
<li>Sushi</li>
<li>Momos</li>
<li>Fried Rice</li>
<li>Omelette</li>
<li>Ice Cream</li>
</ul>

</td>

</tr>

</table>

<hr>

<h2>🧠 DEEP LEARNING MODELS USED</h2>

<ul>
<li>Custom CNN</li>
<li>VGG16</li>
<li>ResNet50</li>
</ul>

<hr>

<h2>⚙️ TECHNOLOGIES USED</h2>

<h3>Programming Language</h3>

<ul>
<li>Python</li>
</ul>

<h3>Libraries</h3>

<ul>
<li>TensorFlow</li>
<li>Keras</li>
<li>OpenCV</li>
<li>NumPy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Seaborn</li>
<li>Scikit-learn</li>
<li>Flask</li>
</ul>

<h3>Frontend</h3>

<ul>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
</ul>

<h3>Backend</h3>

<ul>
<li>Flask</li>
</ul>

<hr>

<h2>🔄 DEEP LEARNING WORKFLOW</h2>

<pre>
Food Image
     ↓
Image Preprocessing
     ↓
Image Resizing
     ↓
Normalization
     ↓
Data Augmentation
     ↓
CNN / VGG16 / ResNet50
     ↓
Model Prediction
     ↓
Food Category Output
</pre>

<hr>

<h2>📌 IMAGE PREPROCESSING TECHNIQUES</h2>

<ul>
<li>Image Resizing</li>
<li>RGB Conversion</li>
<li>Normalization</li>
<li>Data Augmentation</li>
<li>Noise Reduction</li>
<li>Image Scaling</li>
</ul>

<hr>

<h2>📌 DATA AUGMENTATION TECHNIQUES</h2>

<ul>
<li>Rotation</li>
<li>Width Shift</li>
<li>Height Shift</li>
<li>Zoom</li>
<li>Horizontal Flip</li>
<li>Brightness Adjustment</li>
</ul>

<hr>

<h2>📈 MODEL PERFORMANCE</h2>

<table border="1" cellpadding="10">

<tr>
<th>Model</th>
<th>Accuracy</th>
<th>Status</th>
</tr>

<tr>
<td>Custom CNN</td>
<td>92%</td>
<td>Good</td>
</tr>

<tr>
<td>VGG16</td>
<td>95%</td>
<td>Better</td>
</tr>

<tr>
<td><b>ResNet50</b></td>
<td><b>97%</b></td>
<td>Best ✅</td>
</tr>

</table>

<hr>

<h2>📊 EVALUATION METRICS</h2>

<ul>
<li>Accuracy</li>
<li>Precision</li>
<li>Recall</li>
<li>F1-Score</li>
<li>Confusion Matrix</li>
<li>Classification Report</li>
</ul>

<hr>

<h2>🖥️ FLASK WEB APPLICATION</h2>

<h3>Features Included</h3>

<ul>
<li>Upload Food Images</li>
<li>Predict Food Category</li>
<li>Display Confidence Score</li>
<li>User-Friendly Interface</li>
<li>Real-Time Inference</li>
</ul>

<hr>

<h2>📂 PROJECT STRUCTURE</h2>

<pre>
Food-Classification-Using-Deep-Learning/
│
├── dataset/
├── models/
├── static/
├── templates/
├── notebook/
├── app.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>💼 REAL WORLD APPLICATIONS</h2>

<ul>
<li>Smart Restaurants</li>
<li>Food Delivery Platforms</li>
<li>Healthcare Systems</li>
<li>Nutrition Monitoring</li>
<li>AI Food Recognition</li>
</ul>

<hr>

<h2>🚀 FUTURE ENHANCEMENTS</h2>

<ul>
<li>Live Camera Detection</li>
<li>Nutrition Information</li>
<li>Cloud Deployment</li>
<li>Mobile Application</li>
<li>YOLO Food Detection</li>
</ul>

<hr>

<h2>📌 CONCLUSION</h2>

<p>
This project demonstrates how Deep Learning and Transfer Learning techniques can be used to build an accurate food image classification system.
</p>

<p>
Among all models, ResNet50 achieved the best performance with 97% accuracy, making the system suitable for real-world AI applications.
</p>

<hr>

<h2>👨‍💻 AUTHOR</h2>

<p><b>Gainaboina Madhu</b></p>

<hr>

<h2>⭐ GITHUB</h2>

<p>If you found this project useful, give it a ⭐ on GitHub!</p>
```
