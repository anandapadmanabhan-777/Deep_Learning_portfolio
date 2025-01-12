import streamlit as st
def description():
    st.markdown(
        """
        <div class="content-container">
        <h1 class="custom-heading2"> 1. MNIST Digit Recognition:</h1>
        <h4 class="custom-details">A deep learning project that classifies handwritten digits using the MNIST dataset. Implemented with Convolutional Neural Networks (CNNs) for accurate digit recognition.</h4>
        </div>

        """,
        unsafe_allow_html=True,
    )