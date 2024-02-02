# get image GIF 함수
# PNG 함수

import streamlit as st
import pandas as pd
from PIL import Image
import base64
import os

from io import BytesIO
from PIL import Image
import base64
import streamlit as st
import pandas as pd
import os

def load_css_as_string(file_name):
    with open(file_name,'r') as f:
        css = f"""{f.read()}"""
    return css

def local_css(file_name):
    with open(file_name, encoding='UTF8') as f:
        st.markdown(f'''<style>{f.read()}</style>''', unsafe_allow_html=True)


# def set_background(logo_image_path):
#     set_index(logo_image_path)
    

def get_image_base64(image_path):
    image = Image.open(image_path)
    buffered = BytesIO()
    image.save(buffered, format="png")
    image_str = base64.b64encode(buffered.getvalue()).decode()
    return image_str

def set_index(logo_image_path):
    # header/footer/main_context layout css hack
    st.markdown( """ <style>
                @import url(https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css);
                header {
                    visibility : hidden;
                }
                body, body div, p, span {
                    font-family: 'Nanumsquare', 'Malgun Gothic' !important;
                }
                .css-qcqlej{
                    flex-grow:1;
                }
                footer {
                    visibility: visible;
                    background: #2D5AF0;
                }
                .css-164nlkn {
                    display : flex;
                    color : #2D5AF0;
                    max-width : 100%;
                    height : 4rem;
                    padding-top : 1rem;
                    padding-bottom : 1rem
                }
                footer a {
                    visibility: hidden;
                }
                footer {
                    font-family : "Nanumsquare";
                }
                footer:after {
                    visibility: visible; 
                    font-weight: 700;
                    font-size: 15px;
                    color: #FFFFFF;
                    align-self : center;
                }
                .css-z5fcl4 {
                padding-left : 10%;
                padding-right : 10%;
                padding-top : 2rem !important;
                display : flex !important;  
                }

                </style> """, unsafe_allow_html=True)
    

def read_gif(path):
    with open(path, 'rb') as f:
        data = f.read()
        data = base64.b64encode(data).decode("utf-8")
    return data
