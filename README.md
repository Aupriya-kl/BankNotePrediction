# Banknote Authentication Prediction

## Project Overview

This project is designed to predict whether a banknote is authentic or counterfeit using machine learning. The project leverages a machine learning model trained on features extracted from images of banknotes. The model predicts the authenticity of a banknote based on these features. The project includes:
- **Training a machine learning model** using a labeled dataset.
- **Building a FastAPI backend** to serve the trained model for predictions.
- **Saving the model** in a `.pkl` file for reuse in the FastAPI application.

## Files in the Repository

1. **`app.py`**  
   - A FastAPI application that exposes an endpoint (`/predict`) to predict whether a banknote is authentic or counterfeit. The model is loaded from the `model.pkl` file, and predictions are made based on the features of the banknote.

2. **`BankNote_Authentication.csv`**  
   - The dataset used to train the machine learning model. It contains features (such as variance, skewness, and curtosis) and a label (`0` for counterfeit and `1` for authentic).

3. **`BankNotes.py`**  
   - A Python script containing classes and functions used for data processing, model training, and prediction. This file could define functions for data loading, preprocessing, and training the machine learning model.

4. **`model.pkl`**  
   - The trained machine learning model saved using **Pickle**. It contains the trained classifier, which is loaded by the FastAPI application for making predictions.

5. **`requirements.txt`**  
   - A list of Python packages required to run the project, including FastAPI, Uvicorn, and scikit-learn.

6. **`.gitignore`**  
   - A configuration file used to specify which files and directories should be ignored by Git when committing the code. Typically includes temporary files, compiled files, and other unnecessary files (e.g., `.pyc`, `__pycache__`, etc.).
