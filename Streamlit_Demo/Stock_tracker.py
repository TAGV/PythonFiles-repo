import yfinance
import pandas
import streamlit as st


x = st.slider("Select value..")
st.write(x,"squared is",x*x)


# Need to run this from terminal using command : streamlit run Stock_tracker.py
# You will see the output in the web browser