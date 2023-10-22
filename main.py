import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place", help="Input the name of the city")
forecast = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")
view = st.selectbox("Select data to view", ["Temperature", "Sky"])
st.subheader(f"{view} for the next {forecast} days in {place}")