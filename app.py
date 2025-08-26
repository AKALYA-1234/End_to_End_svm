import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open('trained_model.sav', 'rb') as f:
    model = pickle.load(f)

# Page title
st.title("🌸 Iris Flower Prediction (SVM)")

st.subheader("Enter Flower Measurements:")

# Input fields
sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, step=0.1)
sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, step=0.1)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, step=0.1)
petal_width = st.number_input('Petal Width (cm)', min_value=0.0, step=0.1)

# Prediction
if st.button('🔮 Predict'):
    input_data = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    )
    prediction = model.predict(input_data)[0]
    st.success(f"✅ The predicted species is: **{prediction}**")
