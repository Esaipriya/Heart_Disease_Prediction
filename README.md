# Heart_Disease_Prediction
ML Project
# ❤️ Heart Disease Prediction using Machine Learning

This project predicts the likelihood of heart disease using machine learning techniques.  
It includes data preprocessing, model training, evaluation, and a Streamlit web application for real-time prediction.

---

## 📌 Project Overview

Heart disease is one of the world’s leading causes of death.  
This ML-based solution helps diagnose heart disease early using clinical input parameters.

The project covers:

✔ Data preprocessing  
✔ Feature engineering  
✔ Model training (Random Forest)  
✔ Evaluation reports (accuracy, precision, recall, F1-score)  
✔ Saving and loading ML models  
✔ Deployment-ready Streamlit web app  

---

## 📁 Folder Structure
Heart_Disease_Prediction/
│
├── data/
│ └── heart.csv
│
├── notebooks/
│ └── model_training.ipynb
│
├── models/
│ └── RandomForest.sav
│
├── src/
│ ├── train_model.py
│ ├── prediction.py
│ └── utils.py
│
├── app/
│ ├── heart_disease_prediction_web_app.py
│ ├── model_loader.py
│ └── requirements.txt


---

## 📊 Dataset Description

The dataset contains clinical attributes such as:

- Age  
- Sex  
- Chest Pain Type  
- Resting Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Resting ECG  
- Max Heart Rate  
- Oldpeak  
- ST Slope  
- Exercise Angina  

Target variable:

- **HeartDisease** → 1 (Yes), 0 (No)

---

## 🧠 Model

A **Random Forest Classifier** is used to train the model.

### Performance:
- Accuracy: **87–90%**
- Good precision & recall
- Balanced classification report

Model is saved as:  
`models/RandomForest.sav`

---

## ▶️ Run the Streamlit App

### 1️⃣ Install requirements

### 2️⃣ Run the web app


---

## 🚀 Deployment

This Streamlit app can be easily deployed on:
- Streamlit Cloud  
- Render  
- HuggingFace Spaces  

---

## ⭐ Future Enhancements

- Add SHAP explainability  
- Add more ML models for comparison  
- Improve UI styling  
- Add API endpoints  

---

## 👩‍💻 Author

**Esai Priya S**  
AI & Data Science Graduate  
Machine Learning | Python | Streamlit

