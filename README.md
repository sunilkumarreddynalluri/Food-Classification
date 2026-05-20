# Food-Classification
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Food Classification Using Deep Learning</title>

<style>

body{
    margin:0;
    padding:0;
    font-family:Arial, sans-serif;
    background:#f5f7fb;
    color:#333;
    line-height:1.7;
}

header{
    background:linear-gradient(135deg,#ff6b35,#ff914d);
    color:white;
    text-align:center;
    padding:50px 20px;
}

header h1{
    font-size:45px;
    margin-bottom:10px;
}

.badges{
    margin-top:20px;
}

.badge{
    display:inline-block;
    background:white;
    color:#333;
    padding:10px 18px;
    margin:5px;
    border-radius:30px;
    font-size:14px;
    font-weight:bold;
}

.container{
    width:90%;
    max-width:1200px;
    margin:auto;
    padding:30px 0;
}

.section{
    background:white;
    padding:25px;
    margin-bottom:25px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

.section h2{
    color:#ff6b35;
    border-left:6px solid #ff914d;
    padding-left:10px;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:15px;
}

table th{
    background:#ff6b35;
    color:white;
    padding:12px;
}

table td{
    border:1px solid #ddd;
    padding:12px;
}

ul{
    padding-left:20px;
}

.code{
    background:#272822;
    color:#f8f8f2;
    padding:15px;
    border-radius:10px;
    overflow-x:auto;
}

.center{
    text-align:center;
}

footer{
    background:#ff6b35;
    color:white;
    text-align:center;
    padding:25px;
    margin-top:30px;
}

img{
    border-radius:15px;
}

</style>

</head>

<body>

<header>

<h1>🍔 Food Classification Using Deep Learning</h1>

<h3>Custom CNN • VGG16 • ResNet50</h3>

<div class="badges">

<span class="badge">Python 3.10</span>
<span class="badge">TensorFlow</span>
<span class="badge">Keras</span>
<span class="badge">OpenCV</span>
<span class="badge">Flask</span>
<span class="badge">97% Accuracy</span>

</div>

<br>

<img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1400&auto=format&fit=crop" width="100%">

</header>

<div class="container">

<div class="section">

<h2>📖 About The Project</h2>

<p>
Food Classification Using Deep Learning is an AI-powered Computer Vision project that automatically identifies food categories from images using Deep Learning models.
</p>

<p>
This project compares the performance of:
</p>

<ul>
<li>Custom CNN</li>
<li>VGG16 Transfer Learning</li>
<li>ResNet50 Transfer Learning</li>
</ul>

<p>
The system was trained on multiple food categories and achieved high classification accuracy using TensorFlow and Keras.
</p>

</div>

<div class="section">

<h2>🚀 Features</h2>

<table>

<tr>

<td width="50%">

<h3>🧠 Deep Learning Models</h3>

<ul>
<li>Custom CNN</li>
<li>VGG16</li>
<li>ResNet50</li>
</ul>

<h3>📷 Image Processing</h3>

<ul>
<li>Image resizing</li>
<li>Normalization</li>
<li>RGB conversion</li>
<li>Data augmentation</li>
</ul>

</td>

<td width="50%">

<h3>🌐 Web Deployment</h3>

<ul>
<li>Flask integration</li>
<li>Real-time prediction</li>
<li>Upload food images</li>
</ul>

<h3>📊 Evaluation</h3>

<ul>
<li>Accuracy</li>
<li>Precision</li>
<li>Recall</li>
<li>F1-Score</li>
<li>Confusion Matrix</li>
</ul>

</td>

</tr>

</table>

</div>

<div class="section">

<h2>🍕 Food Categories</h2>

<table>

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

</div>

<div class="section">

<h2>⚙️ Deep Learning Workflow</h2>

<div class="code">

<pre>
Food Image
     ↓
Image Preprocessing
     ↓
Data Augmentation
     ↓
CNN / VGG16 / ResNet50
     ↓
Model Prediction
     ↓
Food Category Output
</pre>

</div>

</div>

<div class="section">

<h2>🤖 Models Performance</h2>

<table>

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

</div>

<div class="section">

<h2>🛠️ Technologies Used</h2>

<div class="center">

<img src="https://skillicons.dev/icons?i=python,tensorflow,opencv,flask,html,css,github,vscode">

</div>

</div>

<div class="section">

<h2>📂 Project Structure</h2>

<div class="code">

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

</div>

</div>

<div class="section">

<h2>🌐 Flask Web Application</h2>

<h3>Features Included</h3>

<ul>
<li>Upload food images</li>
<li>Predict food category</li>
<li>Display confidence score</li>
<li>User-friendly interface</li>
<li>Real-time inference</li>
</ul>

</div>

<div class="section">

<h2>🚀 Future Enhancements</h2>

<ul>
<li>📷 Live Camera Detection</li>
<li>🥗 Nutrition Information</li>
<li>☁️ Cloud Deployment</li>
<li>📱 Mobile Application</li>
<li>🎯 YOLO Food Detection</li>
</ul>

</div>

<div class="section">

<h2>💼 Real World Applications</h2>

<ul>
<li>🍽️ Smart Restaurants</li>
<li>🚚 Food Delivery Platforms</li>
<li>🏥 Healthcare Systems</li>
<li>📊 Nutrition Monitoring</li>
<li>🤖 AI Food Recognition</li>
</ul>

</div>

<div class="section">

<h2>👨‍💻 Author</h2>

<h3>Gainaboina Madhu</h3>

</div>

<div class="section">

<h2>⭐ Conclusion</h2>

<p>
This project demonstrates how Deep Learning and Transfer Learning techniques can be used to build an accurate food image classification system.
</p>

<p>
Among all models, ResNet50 achieved the best performance with 97% accuracy, making the system suitable for real-world AI applications.
</p>

</div>

</div>

<footer>

<h2>🌟 If you found this project useful, give it a star on GitHub!</h2>

</footer>

</body>
</html>
```
