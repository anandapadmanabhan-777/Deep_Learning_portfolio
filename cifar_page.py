import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np


def cifar_page():
    st.markdown(
        """
        <h1 class="name-heading">CIFAR-10 Classifier</h1>
        <h3 class="custom-subheader">Upload an image to classify it into one of the CIFAR-10 classes.</h3>
        """,
        unsafe_allow_html=True,
    )

    try:
        # Attempt to load the CIFAR-10 model
        cifar_model = load_model('cifar10_model.keras')
        st.success("CIFAR-10 Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        cifar_model = None  # Set the model to None if it fails to load

    if cifar_model:
        # File uploader for user to upload an image
        uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            try:
                # Process the uploaded image
                image = Image.open(uploaded_image)
                image = image.resize((32, 32))  # Resize to 32x32 for CIFAR-10
                image = np.array(image) / 255.0  # Normalize the image
                image = image.reshape(1, 32, 32, 3)  # Reshape for model input

                # Define the class labels
                class_labels = [
                    "Airplane", "Automobile", "Bird", "Cat", "Deer", 
                    "Dog", "Frog", "Horse", "Ship", "Truck"
                ]

                if st.button("Predict CIFAR-10 Class"):
                    try:
                        # Make the prediction
                        prediction = cifar_model.predict(image)
                        predicted_label = np.argmax(prediction)
                        predicted_class = class_labels[predicted_label]
                        st.subheader(f"Predicted CIFAR-10 Class: {predicted_class}")
                    except Exception as e:
                        st.error(f"Error making prediction: {e}")
            except Exception as e:
                st.error(f"Error processing the image: {e}")
    else:
        st.error("Model not loaded. Cannot make predictions.")

    # Adding a Model View Button
    st.markdown(
        """
        <a href="https://github.com/anandapadmanabhan-777/CIFAR-10_Classification" target="_blank">
            <button class="hyperlink-button">
                View CIFAR-10 Classifier Model
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
