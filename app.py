import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model
model = joblib.load("iris_model.pkl")

# Streamlit page title
st.title("🌸 Iris Flower Prediction App")
st.write("Enter Sepal & Petal measurements to predict the Iris species.")

# User input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Predict button
if st.button("Predict"):
    # Prepare input for model
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    
    # Map class index to name
    target_names = ["Setosa", "Versicolor", "Virginica"]
    predicted_species = target_names[prediction[0]]
    
    st.success(f"🌼 Predicted Iris species: **{predicted_species}**")
