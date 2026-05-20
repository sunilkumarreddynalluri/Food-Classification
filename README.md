# Food-Classification
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Food Classification Using Deep Learning</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    background:#0f172a;
    color:#f8fafc;
    line-height:1.7;
}

.container{
    width:90%;
    max-width:1200px;
    margin:auto;
    padding:40px 0;
}

.hero{
    text-align:center;
    padding:80px 20px;
}

.hero h1{
    font-size:4rem;
    color:#38bdf8;
    margin-bottom:20px;
}

.hero p{
    font-size:1.2rem;
    color:#cbd5e1;
    max-width:900px;
    margin:auto;
}

.badges{
    margin-top:30px;
}

.badges img{
    margin:5px;
}

.banner{
    margin-top:40px;
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}

.banner img{
    width:100%;
    display:block;
}

.section{
    margin-top:80px;
}

.section h2{
    font-size:2.2rem;
    margin-bottom:25px;
    color:#38bdf8;
}

.card{
    background:#1e293b;
    padding:30px;
    border-radius:20px;
    margin-top:25px;
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

.card p{
    color:#e2e8f0;
}

ul{
    margin-left:25px;
    margin-top:15px;
}

li{
    margin-bottom:12px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;
    margin-top:30px;
}

.feature{
    background:#1e293b;
    padding:25px;
    border-radius:20px;
    transition:0.3s;
}

.feature:hover{
    transform:translateY(-8px);
}

.feature h3{
    margin-bottom:15px;
    color:#38bdf8;
}

.table-container{
    overflow-x:auto;
    margin-top:25px;
}

table{
    width:100%;
    border-collapse:collapse;
    background:#1e293b;
    border-radius:15px;
    overflow:hidden;
}

table th{
    background:#38bdf8;
    color:#0f172a;
    padding:15px;
}

table td{
    padding:15px;
    border-bottom:1px solid #334155;
}

.footer{
    text-align:center;
    padding:50px 20px;
    margin-top:80px;
    color:#94a3b8;
}

.code{
    background:#020617;
    padding:20px;
    border-radius:15px;
    overflow:auto;
    margin-top:20px;
    color:#38bdf8;
}

.highlight{
    color:#38bdf8;
    font-weight:600;
}

</style>
</head>

<body>

<div class="container">

    <!-- HERO SECTION -->

    <section class="hero">

        <h1>🍔 Food Classification Using Deep Learning</h1>

        <p>
            An advanced Deep Learning and Computer Vision project that classifies
            food images into multiple categories using Custom CNN,
            VGG16, and ResNet50 architectures.
        </p>

        <div class="badges">

            <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">

            <img src="https://img.shields.io/badge/TensorFlow-Deep_Learning-orange?style=for-the-badge&logo=tensorflow">

            <img src="https://img.shields.io/badge/Keras-CNN-red?style=for-the-badge&logo=keras">

            <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv">

            <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">

            <img src="https://img.shields.io/badge/Accuracy-97%25-success?style=for-the-badge">

        </div>

        <div class="banner">
            <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1400&auto=format&fit=crop">
        </div>

    </section>

    <!-- OVERVIEW -->

    <section class="section">

        <h2>📖 Project Overview</h2>

        <div class="card">

            <p>
                This project focuses on automatic food image classification
                using Deep Learning techniques. The system can recognize
                multiple food categories from uploaded images with high accuracy.
            </p>

            <br>

            <p>
                Three different deep learning models were implemented and compared:
            </p>

            <ul>
                <li>Custom CNN Architecture</li>
                <li>VGG16 Transfer Learning Model</li>
                <li>ResNet50 Transfer Learning Model</li>
            </ul>

            <p>
                The best-performing model, <span class="highlight">ResNet50</span>,
                achieved an impressive <span class="highlight">97% accuracy</span>.
            </p>

        </div>

    </section>

    <!-- FEATURES -->

    <section class="section">

        <h2>🚀 Features</h2>

        <div class="grid">

            <div class="feature">
                <h3>🧠 Deep Learning</h3>
                <p>
                    Implements CNN and Transfer Learning architectures
                    for accurate image classification.
                </p>
            </div>

            <div class="feature">
                <h3>📷 Image Processing</h3>
                <p>
                    Includes preprocessing, normalization,
                    resizing, and augmentation techniques.
                </p>
            </div>

            <div class="feature">
                <h3>🌐 Flask Deployment</h3>
                <p>
                    Real-time web application for food image prediction.
                </p>
            </div>

            <div class="feature">
                <h3>📊 Performance Evaluation</h3>
                <p>
                    Uses accuracy, precision, recall,
                    F1-score, and confusion matrix.
                </p>
            </div>

        </div>

    </section>

    <!-- MODELS -->

    <section class="section">

        <h2>🤖 Models Used</h2>

        <div class="table-container">

            <table>

                <tr>
                    <th>Model</th>
                    <th>Accuracy</th>
                    <th>Description</th>
                </tr>

                <tr>
                    <td>Custom CNN</td>
                    <td>92%</td>
                    <td>Built and trained from scratch using convolution layers.</td>
                </tr>

                <tr>
                    <td>VGG16</td>
                    <td>95%</td>
                    <td>Transfer learning model pretrained on ImageNet dataset.</td>
                </tr>

                <tr>
                    <td>ResNet50</td>
                    <td>97%</td>
                    <td>Best-performing residual neural network architecture.</td>
                </tr>

            </table>

        </div>

    </section>

    <!-- WORKFLOW -->

    <section class="section">

        <h2>⚙️ Deep Learning Workflow</h2>

        <div class="card">

<div class="code">

Dataset Collection  
↓  
Image Preprocessing  
↓  
Data Augmentation  
↓  
Train/Test Split  
↓  
Model Training  
↓  
Model Evaluation  
↓  
Flask Deployment  

</div>

        </div>

    </section>

    <!-- TECHNOLOGIES -->

    <section class="section">

        <h2>🛠️ Technologies Used</h2>

        <div class="grid">

            <div class="feature">
                <h3>Python</h3>
                <p>Main programming language used for development.</p>
            </div>

            <div class="feature">
                <h3>TensorFlow & Keras</h3>
                <p>Used for building and training deep learning models.</p>
            </div>

            <div class="feature">
                <h3>OpenCV</h3>
                <p>Used for image preprocessing and computer vision operations.</p>
            </div>

            <div class="feature">
                <h3>Flask</h3>
                <p>Backend framework used for deployment.</p>
            </div>

        </div>

    </section>

    <!-- APPLICATIONS -->

    <section class="section">

        <h2>💼 Real World Applications</h2>

        <div class="card">

            <ul>
                <li>🍽️ Smart Restaurants</li>
                <li>📦 Food Delivery Platforms</li>
                <li>🏥 Healthcare & Nutrition Tracking</li>
                <li>🤖 AI Food Recognition Systems</li>
                <li>📱 Mobile Food Scanner Applications</li>
            </ul>

        </div>

    </section>

    <!-- FUTURE -->

    <section class="section">

        <h2>🚀 Future Enhancements</h2>

        <div class="grid">

            <div class="feature">
                <h3>📷 Live Camera Detection</h3>
                <p>Real-time food recognition using webcam.</p>
            </div>

            <div class="feature">
                <h3>🥗 Nutrition Analysis</h3>
                <p>Display calorie and nutrition information.</p>
            </div>

            <div class="feature">
                <h3>☁️ Cloud Deployment</h3>
                <p>Deploy on AWS, GCP, or Heroku.</p>
            </div>

            <div class="feature">
                <h3>📱 Mobile App</h3>
                <p>Android and iOS food recognition application.</p>
            </div>

        </div>

    </section>

    <!-- CONCLUSION -->

    <section class="section">

        <h2>⭐ Conclusion</h2>

        <div class="card">

            <p>
                This project demonstrates how Deep Learning and Computer Vision
                can be combined to build an intelligent food classification system.
            </p>

            <br>

            <p>
                By comparing Custom CNN, VGG16, and ResNet50 models,
                the project clearly shows the effectiveness of Transfer Learning
                for image classification tasks.
            </p>

            <br>

            <p>
                The final Flask deployment makes the system practical,
                interactive, and suitable for real-world applications.
            </p>

        </div>

    </section>

    <!-- FOOTER -->

    <div class="footer">

        <h3>👨‍💻 Developed By Gainaboina Madhu</h3>

        <br>

        <p>
            If you found this project useful, don't forget to ⭐ the repository.
        </p>

    </div>

</div>

</body>
</html>
```
