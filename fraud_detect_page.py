import streamlit as st
import pandas as pd
from keras.models import load_model

def fraud_detect_page():
    st.markdown(
            """
            <h1 class="name-heading">Credit Card Fraud Detection</h1>
            <h3 class="custom-subheader">Fill out the form below to predict whether a transaction is fraudulent or not.</h3>
            """,
            unsafe_allow_html=True,
        )
    # Try to load the trained model
    try:
        fraud_detect_model = load_model('fraud_detect_model.keras')
        st.success("Model loaded successfully.")
        
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        fraud_detect_model = None  # Set the model to None if it fails to load

    if fraud_detect_model:  # Only show the form if the model is successfully loaded
        # Input form
        with st.form("fraud_form"):
            try:
                # Transaction Inputs
                transaction_id = st.number_input("Transaction ID", min_value=1)
                amount = st.number_input("Amount", min_value=0.0, step=1.0)
                merchant_id = st.number_input("Merchant ID", min_value=1)
                transaction_type = st.selectbox("Transaction Type", options=["Refund", "Purchase"])

                # Date Inputs (for TransactionDate encoding)
                year = st.number_input("Year", min_value=2000, max_value=2100, step=1)
                month = st.number_input("Month", min_value=1, max_value=12, step=1)
                day = st.number_input("Day", min_value=1, max_value=31, step=1)
                hour = st.number_input("Hour", min_value=0, max_value=23, step=1)

                # Submit button
                submitted = st.form_submit_button("Predict Fraud")

                if submitted:
                    try:
                        # Encode categorical inputs
                        transaction_type_encoded = 1 if transaction_type == "Purchase" else 0

                        # Create input DataFrame with encoded columns
                        input_data = pd.DataFrame({
                            "TransactionID": [transaction_id],
                            "Amount": [amount],
                            "MerchantID": [merchant_id],
                            "TransactionType": [transaction_type_encoded],
                            "Year": [year],
                            "Month": [month],
                            "Day": [day],
                            "Hour": [hour]
                        })

                        # Ensure the order of columns matches the model's training data
                        expected_columns = [
                            "TransactionID", "Amount", "MerchantID", "TransactionType",
                            "Year", "Month", "Day", "Hour"
                        ]
                        input_data = input_data[expected_columns]

                        # Make prediction
                        prediction = fraud_detect_model.predict(input_data)
                        result = "Fraudulent Transaction" if prediction[0][0] > 0.5 else "Non-Fraudulent Transaction"

                        # Display result
                        st.subheader(result)

                    except Exception as e:
                        st.error(f"Error making prediction: {e}")

            except Exception as e:
                st.error(f"Error processing form input: {e}")

    else:
        st.error("Model not loaded. Cannot show prediction form.")

    # Adding a Model View Button
    st.markdown(
        """
        <a href="https://github.com/anandapadmanabhan-777/Credit_Card_Fraud_Detection" target="_blank">
            <button class="hyperlink-button">
                View Fraud Detection Model
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
