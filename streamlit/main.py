import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from PIL import Image

username=st.sidebar.text_input('请输入用户名')
password=st.sidebar.text_input('请输入密码')

st.header(':red[W]:blue[e]:green[lcome]')
temp_img=Image.open('streamlit_img/school.jpg')
st.image(temp_img,width=240)
if username=='2523253262' and password=='123456':
    st.header('示例')
    st.write('以下是经过AI处理过的效果图')
    image1=Image.open('streamlit_img/example.jpg')
    st.image(image1)
    st.header('视频演示效果图')
    vedio = open('streamlit_img/vedio1.mp4', 'rb')
    vedio_byte = vedio.read()
    st.video(vedio_byte)
    image=st.file_uploader('请上传一张图片')
    col1,col2=st.columns(2)
    if image:
        with col1:
            st.header('原图')
            st.image(image)
        with col2:
            st.header(':blue[处理后的图片]')
            st.image(image)


