import streamlit as st
import pandas as pd
import numpy as np
import pickle

df=pd.read_csv("Cleaned_Data.csv")
model=pickle.load(open("LinearRegressionModel.pkl","rb"))

st.title("House Price Predictor")
st.markdown("---")

s1=st.selectbox("Select The Area",key=1,options=df["location"].unique())
s2=st.slider("Select The Total Square Feet",min_value=(df["total_sqft"].min()),max_value=(df["total_sqft"].max()))
s3=st.selectbox("Select The Total No of Bathrooms you want",key=2,options=sorted(df["bath"].unique()))
s4=st.selectbox("Select The BHK",key=3,options=sorted(df["bhk"].unique()))
btn=st.button("Predict The Price")
if btn:
    result = model.predict(pd.DataFrame(columns=["location", "total_sqft", "bath", "bhk"], data=
    np.array([s1, s2, s3, s4]).reshape(1, 4)))
    if result:
        if result < 0:
            st.subheader("Price Cannot Be Predicted")
        else:
            st.subheader(f"{result[0]:.2f} lakhs")
    else:
        st.subheader("Price Cannot be Predicted")