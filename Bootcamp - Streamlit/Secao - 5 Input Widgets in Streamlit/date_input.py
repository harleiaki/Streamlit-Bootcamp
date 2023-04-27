import streamlit as st
import datetime

d = st.date_input (
    "When is your birthday?",
    datetime.date(2022,3,6))

st.write("Your birthday is:",d)
