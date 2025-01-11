import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np


def fashion_page():
    st.markdown(
        """
        <h1 class="custom-heading2">Fashion-MNIST Classifier</h1>
        <h3 class="custom-subheader">Upload an image of a fashion item to classify it.</h3>
        """,
        unsafe_allow_html=True,
    )

    try:
        # Attempt to load the Fashion-MNIST model
        fashion_mnist_model = load_model('fashion_mnist_model.keras')
        st.success("Fashion-MNIST Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        fashion_mnist_model = None  # Set the model to None if it fails to load

    if fashion_mnist_model:
        # File uploader for user to upload an image
        uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            try:
                # Process the uploaded image
                image = Image.open(uploaded_image)
                image = image.convert('L')  # Convert to grayscale
                image = image.resize((28, 28))  # Resize to 28x28 for Fashion-MNIST
                image = np.array(image) / 255.0  # Normalize the image
                image = image.reshape(1, 28, 28, 1)  # Reshape for model input

                # Define the class labels
                class_labels = [
                    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
                    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
                ]

                if st.button("Predict Fashion Item"):
                    try:
                        # Make the prediction
                        prediction = fashion_mnist_model.predict(image)
                        predicted_label = np.argmax(prediction)
                        predicted_class = class_labels[predicted_label]
                        st.subheader(f"Predicted Fashion Item: {predicted_class}")
                    except Exception as e:
                        st.error(f"Error making prediction: {e}")
            except Exception as e:
                st.error(f"Error processing the image: {e}")
    else:
        st.error("Model not loaded. Cannot make predictions.")
