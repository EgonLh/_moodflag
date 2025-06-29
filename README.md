# Mood Swing Prediction API and Streamlit Web App

## Problem Statement

In today's fast-paced world, mental health challenges like mood swings often go unnoticed or undiagnosed, leading to severe consequences for individuals' well-being. While professional care is essential, early detection using accessible and non-invasive methods can help people become more aware of their mental state and seek support when necessary. This project aims to provide a lightweight, AI-powered solution that predicts mood swing tendencies based on survey-style inputs, making it easier to monitor and reflect on mental health.

## Project Overview

- A **FastAPI-based RESTful API** for making predictions.
- A **Streamlit web application** for users to interact with the model via a simple UI.

## Features

- Input form for mental health and lifestyle-related data
- Real-time mood swing prediction
- Simple API to connect front-end and back-end

## Tech Stack

- Python 3.10+
- Scikit-learn
- XGBoost
- Pandas, NumPy
- FastAPI
- Streamlit
- Joblib

## Folder Structure

```bash
.
├── app/
│   ├── main.py                 # FastAPI app for serving predictions
│   └── model/
│       ├── xgb_model.pkl       # Trained XGBoost model
│       ├── encoder.pkl         # Saved label encoders (as a dictionary)
│       └── __init__.py
│
├── streamlit_app/
│   ├── app.py                  # Streamlit web application
│   └── utils.py                # Utility functions for the UI
│
├── training/
│   ├── train_model.py          # Script to train and save the model
│   ├── preprocess.py           # Script to encode and preprocess data
│   └── utils.py                # Helper functions for training pipeline
│
├── data/
│   ├── raw_data.csv            # Original dataset
│   └── cleaned_data.csv        # Cleaned and preprocessed dataset
│
├── tests/
│   ├── test_api.py             # Test cases for API endpoints
│   └── test_model.py           # Unit tests for model logic
│
├── requirements.txt            # Python dependencies
└── README.md

```

# MoodFlag Project Resources


Frontend  
- **Live App:**  
  [ MoodFlag Streamlit App](https://moodflag-yxmsxx9v3vkkrjhphbqopn.streamlit.app/)


Backend (API)  
- **API Docs (Swagger UI):**  
  [📘 MoodFlag API Documentation](https://moodflag-api.onrender.com/docs)


Dataset & Model Exploration  
- **Kaggle Notebook:**  
  [📈 ML Applications to Mental Health Diagnosis](https://www.kaggle.com/code/maxboonjindasup/ml-applications-to-mental-health-diagnosis#Model-Building-&-Comparisons)

---
