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
        'crim': 3.61, 'zn': 11.36, 'indus': 11.14, 'chas': 0.0, 
        'nox': 0.55, 'rm': 6.28, 'age': 68.57, 'dis': 3.80, 
        'rad': 9.55, 'tax': 408.24, 'ptratio': 18.46, 'black': 356.67, 'lstat': 12.65
    }])

model = load_model()

st.title("🏡 Boston House Price Predictor")
st.markdown("Adjust the specific property characteristics below to estimate its value based on historical market data.")

st.sidebar.header("Configure Property Features")

# Sidebar inputs
nr_rooms = st.sidebar.slider("Number of Rooms", min_value=1.0, max_value=10.0, value=3.0, step=1.0)
students_per_classroom = st.sidebar.slider("Students per Teacher Ratio", min_value=12.0, max_value=22.0, value=18.46, step=0.1)
distance_to_town = st.sidebar.slider("Distance to Employment Centers", min_value=1.0, max_value=12.0, value=3.80, step=0.1)
next_to_river = st.sidebar.checkbox("Next to Charles River")
pollution = st.sidebar.slider("Nitric Oxide Concentration", min_value=0.00, max_value=1.00, value=0.55, step=0.01)
amount_of_poverty = st.sidebar.slider("% Lower Status Population", min_value=1.0, max_value=40.0, value=12.6, step=0.1)

st.markdown("---")
if st.button("Predict Property Value", type="primary"):
    with st.spinner("Calculating valuation..."):
        # Load the baseline property stats
        property_stats = get_default_features()
        
        # Update only the features the user adjusted in the sidebar
        property_stats.loc[0, 'rm'] = nr_rooms
        property_stats.loc[0, 'ptratio'] = students_per_classroom
        property_stats.loc[0, 'dis'] = distance_to_town
        property_stats.loc[0, 'chas'] = 1 if next_to_river else 0
        property_stats.loc[0, 'nox'] = pollution
        property_stats.loc[0, 'lstat'] = amount_of_poverty
        
        try:
            # Make the log price prediction
            log_estimate = model.predict(property_stats)[0]
            
            # Convert the log estimate back to actual dollar values
            actual_price = np.exp(log_estimate) * 1000
            
            st.success(f"### Estimated Property Value: ${actual_price:,.2f}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Prediction Error. Please verify the model features. Details: {e}")
