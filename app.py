import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configuration
st.set_page_config(page_title="Boston Real Estate Predictor", page_icon="🏡", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load('log_regr_model.pkl')

@st.cache_data
def get_default_features():
    return pd.DataFrame([{
        'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.14, 'CHAS': 0.0, 
        'NOX': 0.55, 'RM': 6.28, 'AGE': 68.57, 'DIS': 3.80, 
        'RAD': 9.55, 'TAX': 408.24, 'PTRATIO': 18.46, 'B': 356.67, 'LSTAT': 12.65
    }])

model = load_model()

st.title("🏡 Boston House Price Predictor")
st.markdown("Adjust the specific property characteristics below to estimate its value based on historical market data.")

st.sidebar.header("Configure Property Features")

# Sidebar inputs
nr_rooms = st.sidebar.slider("Number of Rooms (RM)", min_value=3.0, max_value=9.0, value=6.28, step=0.1)
students_per_classroom = st.sidebar.slider("Students per Teacher (PTRATIO)", min_value=12.0, max_value=22.0, value=18.46, step=0.1)
distance_to_town = st.sidebar.slider("Distance to Employment (DIS)", min_value=1.0, max_value=12.0, value=3.80, step=0.1)
next_to_river = st.sidebar.checkbox("Next to Charles River (CHAS)")
pollution = st.sidebar.slider("Nitric Oxide Concentration (NOX)", min_value=0.3, max_value=0.9, value=0.55, step=0.01)
amount_of_poverty = st.sidebar.slider("% Lower Status Population (LSTAT)", min_value=1.0, max_value=40.0, value=12.65, step=0.1)

st.markdown("---")
if st.button("Predict Property Value", type="primary"):
    with st.spinner("Calculating valuation..."):
        # Load the baseline property stats
        property_stats = get_default_features()
        
        # Update only the features the user adjusted in the sidebar
        property_stats.loc[0, 'RM'] = nr_rooms
        property_stats.loc[0, 'PTRATIO'] = students_per_classroom
        property_stats.loc[0, 'DIS'] = distance_to_town
        property_stats.loc[0, 'CHAS'] = 1 if next_to_river else 0
        property_stats.loc[0, 'NOX'] = pollution
        property_stats.loc[0, 'LSTAT'] = amount_of_poverty
        
        try:
            # Make the log price prediction
            log_estimate = model.predict(property_stats)[0]
            
            # Convert the log estimate back to actual dollar values
            actual_price = np.exp(log_estimate) * 1000
            
            st.success(f"### Estimated Property Value: ${actual_price:,.2f}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Prediction Error. Please verify the model features. Details: {e}")
            