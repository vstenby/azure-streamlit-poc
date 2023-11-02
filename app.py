import streamlit as st

#Make the app wide.
st.set_page_config(layout="wide")

st.markdown("# FCP Streamlit App")
st.write("This is a proof of concept Streamlit app.")

#To begin with, let's add a text field that simply just counts the letters.
s = st.text_input("Enter some text here:")
st.write("Your string has", len(s), "characters.")

st.write('Hello from Python!')