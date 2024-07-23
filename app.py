import streamlit as st
import pickle
import numpy as np

# Load model
with open("model_file.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
st.title("Prediksi Kesehatan Janin")

# Input form
with st.form(key='prediction_form'):
    abnormal_short_term_variability = st.text_input("Abnormal Short Term Variability:", "")
    percentage_of_time_with_abnormal_long_term_variability = st.text_input("Percentage of Time with Abnormal Long Term Variability:", "")
    histogram_mode = st.text_input("Histogram Mode:", "")
    histogram_mean = st.text_input("Histogram Mean:", "")
    histogram_median = st.text_input("Histogram Median:", "")
    histogram_variance = st.text_input("Histogram Variance:", "")
    submit_button = st.form_submit_button(label='Predict')

# Prediction logic
if submit_button:
    try:
        # Convert inputs to float
        input_data = np.array([[
            float(abnormal_short_term_variability),
            float(percentage_of_time_with_abnormal_long_term_variability),
            float(histogram_mode),
            float(histogram_mean),
            float(histogram_median),
            float(histogram_variance)
        ]])

        # Predict using loaded model
        prediction = model.predict(input_data)[0]

        # Map prediction to health status
        if prediction == 1.0:
            health_status = 'Normal'
        elif prediction == 2.0:
            health_status = 'Suspect'
        elif prediction == 3.0:
            health_status = 'Pathological'
        else:
            health_status = 'Unknown'

        st.success(f'Health Status: {health_status}')

    except ValueError as e:
        st.error(f'Invalid value: {e}')
    except Exception as e:
        st.error(f'Unexpected error: {e}')
