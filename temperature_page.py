import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

def temperature_page():
    st.markdown(
        """
        <h1 class="name-heading">Temperature Prediction</h1>
        <h3 class="custom-subheader">Fill out the form below to predict the temperature of the next day using CNN-RNN hybrid model.</h3>
        """,
        unsafe_allow_html=True,
    )

    # Load the trained model
    try:
        model = load_model('Predict_Temperature.keras')
        st.success("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        model = None

    if model:
        # Load historical weather data (for example, the last 13 rows)
        try:
            historical_data = pd.read_csv("weather_data_new.csv")  # Replace with the path to your data file
            historical_data['Date/Time'] = pd.to_datetime(historical_data['Date/Time'])
            historical_data.set_index('Date/Time', inplace=True)
            historical_data = historical_data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']]
            historical_data = historical_data.tail(13)  # Get the last 13 data points
        except Exception as e:
            st.error(f"Error loading historical data: {e}")
            historical_data = None

        if historical_data is not None:
            

            # Input form for user data
            with st.form(key="input_form"):
                st.header("Input Features")
                Temp_C = st.number_input("Temperature (°C): Range: -23.3 to 33.0", min_value=-23.3, max_value=33.0, value=20.0, step=0.1)
                Dew_Point_Temp_C = st.number_input("Dew Point Temperature (°C): Range: -28.5 to 24.4", min_value=-28.5, max_value=24.4, value=10.0, step=0.1)
                Rel_Hum_ = st.number_input("Relative Humidity (%): Range: 18.0 to 100.0", min_value=18.0, max_value=100.0, value=60.0, step=1.0)
                Wind_Speed_ = st.number_input("Wind Speed (km/h): Range: 0.0 to 83.0", min_value=0.0, max_value=83.0, value=15.0, step=1.0)
                Visibility_km = st.number_input("Visibility (km): Range: 0.2 to 48.3", min_value=0.2, max_value=48.3, value=10.0, step=1.0)
                Press_kPa = st.number_input("Pressure (kPa): Range: 97.52 to 103.65", min_value=97.52, max_value=103.65, value=100.3, step=0.1)
                
                # Add predict button
                predict_button = st.form_submit_button(label="Predict")

            # Process input and make predictions if the button is clicked
            if predict_button:
                try:
                    # Convert inputs to a DataFrame
                    input_data = np.array([[Temp_C, Dew_Point_Temp_C, Rel_Hum_, Wind_Speed_, Visibility_km, Press_kPa]])

                    # Combine the historical data with the user input (this will be your input sequence)
                    combined_data = pd.DataFrame(input_data, columns=['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa'])
                    combined_data = pd.concat([historical_data, combined_data], ignore_index=True)

                    # Scale the data (use the scaler that was fit on your original training data)
                    scaler = StandardScaler()
                    scaled_input = scaler.fit_transform(combined_data)  # Scaling combined data

                    # Reshape the data to fit the model's input shape (14 time steps, 6 features)
                    scaled_input = scaled_input.reshape(1, 14, 6)

                    # Make predictions
                    prediction = model.predict(scaled_input)
                    st.divider()
                    st.subheader(f"Predicted Temperature (°C): {prediction[0][0]:.2f}")
                except Exception as e:
                    st.error(f"Error in processing or making prediction: {e}")
            
    # Adding a Model View Button
    st.markdown(
        """
        <a href="https://github.com/anandapadmanabhan-777/Temperature_Prediction_App" target="_blank">
            <button class="hyperlink-button">
                View Temperature Prediction Model
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )