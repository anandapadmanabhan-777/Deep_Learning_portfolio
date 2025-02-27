import streamlit as st
def description():
    st.markdown(
        """
        <div class="content-container">

        <h3 class="custom-heading3">1. <u>Customer Churn Prediction</u>:</h3>
        <h5 class="custom-details">Built an Artificial Neural Network (ANN) model to predict customer churn based on customer attributes, providing actionable insights to enhance retention strategies.</h5>

        <h3 class="custom-heading3">2. <u>Credit Card Fraud Detection</u>:</h3>
        <h5 class="custom-details">A machine learning model to detect fraudulent credit card transactions, ensuring high accuracy and reducing false positives through advanced anomaly detection techniques.</h5>

        <h3 class="custom-heading3">3. <u>MNIST Digit Recognition</u>:</h3>
        <h5 class="custom-details">A deep learning project that classifies handwritten digits using the MNIST dataset. Implemented with Convolutional Neural Networks (CNNs) for accurate digit recognition.</h5>

        <h3 class="custom-heading3">4. <u>Fashion MNIST Classification</u>:</h3>
        <h5 class="custom-details">A machine learning project for categorizing Zalando’s fashion items (shirts, shoes, bags, etc) into predefined classes using neural networks.</h5>

        <h3 class="custom-heading3">5. <u>Temperature Prediction</u>:</h3>
        <h5 class="custom-details">A time-series forecasting project utilizing a CNN-RNN hybrid model to predict future temperature trends based on historical weather data, enabling accurate environmental analysis and planning.</h5>

        <h3 class="custom-heading3">5. <u>CIFAR-10 Classification</u>:</h3>
        <h5 class="custom-details">A machine learning project for classifying 60,000 32x32 color images into 10 predefined classes (airplane, car, bird, etc) using convolutional neural networks (CNNs).</h5>

        </div>

        """,
        unsafe_allow_html=True,
    )