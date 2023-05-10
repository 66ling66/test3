import streamlit as st
from PIL import Image

img=Image.open('example.jpg')

st.image(img)