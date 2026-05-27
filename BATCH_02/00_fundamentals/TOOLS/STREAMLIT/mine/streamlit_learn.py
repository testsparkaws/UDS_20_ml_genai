# streamlit run streamlit_learn.py
import streamlit as st

st.set_page_config(
    page_title="streamlit demo app",
    page_icon="🚀",
    # layout="wide",
    layout="centered"
)

# <h1>
st.title("Ultimate Data Science")

# <h3>
st.subheader("Level 1")

# <p>
st.write("This is batch number 2 of ultimate data science bootcamp")

# Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Dashboard", "Settings"])

with tab1:
    # print("Welcome to home tab")
    st.write("Welcome to Home tab!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Left section (HOME)!")
        st.button("Click Left Section Button", type="primary")

    with col2:
        st.write("Centre section (HOME)!")
        st.button("Click Centre Section Button", type="secondary")

    with col3:
        st.write("Right section (HOME)!")
        st.button("Click Right Section Button", type="tertiary")

with tab2:
    st.write("Welcome to Dashboard tab!")

with tab3:
    st.write("Welcome to Settings tab!")

st.divider()

st.subheader("Level 2")

# container
with st.container(height=200, border=True):
    for i in range(100):
        st.write(f"Hello {i}")

st.divider()

st.subheader("Level 3 - Widgets")

# input widgets

if st.button("Say Hello"):
    st.write("Hello there!")

st.link_button("Streamlit Widget Page Redirect", url="https://docs.streamlit.io/develop/api-reference/widgets")

a = 0
print(a)
name = st.text_input("Enter Name")
a+=1
print(a)
print(name)
st.write(f"Hello {name}!")

count = 0
if st.button("Click here to add 1 to the count"):
    count+=1
    st.write(f"Hello there!, the current count value is {count}")


