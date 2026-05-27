# streamlit run streamlit_learn.py

import streamlit as st

st.set_page_config(page_title="streamlist demo app", page_icon="🚀", layout = "centered")

# <H1>
st.title("Ultimate Data Science")

# <H3>
st.subheader("Level 1")

# <p>
st.write("This is batch number 2 of ultimate data science bootcamp")

## tabs 
home_tab , dashboard_tab, settings_tab = st.tabs(["Home","Dashboard","Settings"])


################ TABS ########################
with home_tab:
    st.write("Welcome to Home Tab") 

    col1 , col2, col3 = st.columns(3)

    with col1:
        st.write("Left Section(HOME)!")
        st.button("CLick Left Section Button", type="primary")

    with col2:
        st.write("Center Section(HOME)!")
        st.button("CLick Center Section Button", type="secondary")

    with col3:
        st.write("Right Section(HOME)!")
        st.button("CLick Right Section Button", type="tertiary")

with dashboard_tab:
    st.write("Welcome to Dashboard Tab")

with settings_tab:
    st.write("Welcome to Settings tab!")

st.divider()
st.subheader("Level 2")

#container 
with st.container(height = 200, border = True):
    for i in range(100):
        st.write(f"Hello {i}")

st.divider()
st.subheader("Level 3 - Widgets")

## INput Widgets 
if st.button("Say Hello"):
    st.write("Hello there!")

st.link_button("streamlit Widget Page Redirect", url = "https://docs.streamlit.io/develop/api-reference/widgets")


print(">>>>>>>>>> START")
a = 0 
print(a)

name = st.text_input("Enter Name")
a+=1 
print(a)
print(name)
st.write(f"Hello {name}!")
print(">>>>>>>>>> END")

######################################
count = 0 
if st.button("clikc here to add 1 to the count"):
    count+=1
    st.write(f"Hello there!, the current count value is {count}")

st.divider()

u_name = st.text_input("User Name")
p_u_name = st.text_input("Password", type = "password")
bio = st.text_area("Tell us about yourself", height = 100)

st.divider()
st.subheader("Level 4 - Widgets")

####################################
import datetime 
today = datetime.date.today()
picked_date = st.date_input("Pick a date", today)
st.write(picked_date)

################
st.divider()
uploaded_file = st.file_uploader("Upload a CSV", type=["csv","txt"])
print(f"uploaded_file: {uploaded_file}")

from io import StringIO

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()

    st.write(f"{type(uploaded_file)}")
    st.write(f"{type(string_data)}")

    st.write(f"File Contents: ")
    st.code(string_data, language = "text")

    st.write("File Uploaded!!")
    st.success("File Uploaded!!")

st.warning("File loading warning!")
st.error("Error!")
st.info("Here is a helpful tip!")

st.divider()

################################## 
if 'count' not in st.session_state:
    st.session_state.count = 0 

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Hello there!, the current count value is {st.session_state.count}")

########
st.divider()

st.title("Main Title") 
st.header("Section Header") # Medium 
st.subheader("Sub-section") # small 

st.markdown("We have **bold** in this statement.")
st.markdown("<h1 style='color: blue;'>Custom Html</h1>", unsafe_allow_html=True)

st.divider()


st.subheader("Level 5 - Extra")

########################################
import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randn(10,2), columns=['A','B'])
#print(df)
st.write("Streamlit Dataframe visualization")
st.dataframe(df)

st.write("stremlit Dataframe brachart")
st.bar_chart(df)

# 
#st.image(r'')

st.divider()

###########################
# import time

# bar = st.progress(0)
# for percent in range(100):
#     time.sleep(0.1)
#     bar.progress(percent + 1)

# st.divider()

################## 
# text_to_save = "1,2,3,4,5"
# st.download_button(
#     label="Download text file",
#     data =text_to_save,
#     file_name="dummy_csv.txt",
#     mime ="text/plain"
# )

import pymupdf