
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

# Map numerical outputs to categories
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# Streamlit app
def main():
    st.title("Iris Flower Species Prediction")
    st.write("Adjust the sliders for input values and get the predicted flower species!")

    # Input sliders
    sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, step=0.1, value=5.0)
    sepal_width = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, step=0.1, value=3.0)
    petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, step=0.1, value=4.0)
    petal_width = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, step=0.1, value=1.0)

    # Prediction
    if st.button("Predict"):
        input_features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(input_features)[0]
        st.success(f"The predicted species is: {species_mapping[prediction]}")

if __name__ == "__main__":
    main()
