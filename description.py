import streamlit as st
def description():
    st.markdown(
        """
        <div class="content-container">

        <h3 class="custom-heading3">1. Customer Churn Prediction:</h3>
        <h4 class="custom-details">Built an Artificial Neural Network (ANN) model to predict customer churn based on customer attributes, providing actionable insights to enhance retention strategies.</h4>

        <h3 class="custom-heading2">2. Credit Card Fraud Detection:</h3>
        <h4 class="custom-details">A machine learning model to detect fraudulent credit card transactions, ensuring high accuracy and reducing false positives through advanced anomaly detection techniques.</h4>

        <h3 class="custom-heading2">3. MNIST Digit Recognition:</h3>
        <h4 class="custom-details">A deep learning project that classifies handwritten digits using the MNIST dataset. Implemented with Convolutional Neural Networks (CNNs) for accurate digit recognition.</h4>

        <h3 class="custom-heading2">4. Fashion MNIST Classification:</h3>
        <h4 class="custom-details">A machine learning project for categorizing Zalando’s fashion items (shirts, shoes, bags) into predefined classes using neural networks.</h4>

        <h3 class="custom-heading2">5. Temperature Prediction:</h3>
        <h4 class="custom-details">A time-series forecasting project utilizing a CNN-RNN hybrid model to predict future temperature trends based on historical weather data, enabling accurate environmental analysis and planning.</h4>


        </div>

        """,
        unsafe_allow_html=True,
    )