# 🎓 College Exam Pass-Fail Predictor

A machine learning web application that predicts whether a college student will pass or fail an exam based on previous exam score, study hours, and a students sleep the night before the Exam. Built using **Python**, **Flask**, and **Logistic Regression Model** trained on Real Student Data, with a lightweight and modern frontend interface. This project demonstrates the deployment of a trained ML model via an API endpoint. Model Follows an EDA -> Proprocessing -> Splitting -> Training Machine learning Development Cycle.

---

## Video Demonstration, Click on Thumbnail Below!
[![Watch the video](https://img.youtube.com/vi/FLkFcHs1KbQ/hqdefault.jpg)](https://www.youtube.com/watch?v=FLkFcHs1KbQ)




Note: The app UI says “Pass/Fail Predictor,” but this was later rebranded as “College Exam Predictor.” Functionality remains the same.

## 🛠️ Tools & Technologies

- **Python** — Core programming language  
- **Flask** — Backend web framework for API creation  
- **scikit-learn** — Machine learning library (logistic regression)  
- **pandas** — Data manipulation and CSV handling   
- **Pickle** — Model serialization (`logistic_regression.pkl`)  
- **HTML/CSS/JS (Frontend)** — Optional interface for input/output  
- **cURL / Postman** — For API testing  
- **Git & GitHub** — Version control and collaboration  

---

## ✨ Features

- ✅ **ML-Based Prediction**: Logistic regression predicts "pass" or "fail" for Students' Next Exam with **90% Accuracy (Model Performance)**
- ✅ **RESTful Flask API**: Exposes a `/predict` route for JSON requests
- ✅ **ML Input Features**: Uses `hours studied` and `test score`
- ✅ **Auto Model Loading**: Pretrained `.pkl` model is loaded on startup
- ✅ **Simple Frontend UI**: Users can test predictions visually
- ✅ **Educational Dataset**: Uses Real World Kaggle CSV data to train and evaluate model
- ✅ **Deployable**: Flask app ready to deploy to AWS, Render, or Heroku


## 🚧 Work in Progress 

07/05/25 - * UI was Upgraded to a Cleaner and Techno Design 

* Will soon Deploy to AWS EC2 Server or Vercel

## 🚀 Getting Started

git clone https://github.com/cabrerajulian401/Exam-Pass-Fail-Predictor.git

Make sure to install Dependencies: pip install -r requirements.txt


1. Navigate to Backend: cd Backend

2. Start Flask Server: python app.py

3. Server will run on: http://localhost:5000/predict

4. Open HTML in Live Server via VS Code Extension

5. Start Making Predictions! 
