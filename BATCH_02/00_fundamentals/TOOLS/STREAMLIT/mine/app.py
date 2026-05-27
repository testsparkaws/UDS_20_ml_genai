import streamlit as st 

st.title("Streamlit Application")
st.write("this is streamlit demo app")

name = st.text_input("enter your name ")
st.write(name)
st.button("TestButton", type = "primary")
st.write("END")

# streamlit run app.py
