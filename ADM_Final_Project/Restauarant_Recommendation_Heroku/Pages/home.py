import streamlit as st
from PIL import Image

def home_func():
    image = Image.open('./images/main.jpg')
    st.image(image, use_column_width=True)