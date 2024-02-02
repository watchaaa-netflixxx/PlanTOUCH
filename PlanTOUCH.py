#PlanTOUCH 시작 페이지
#  background-image: url("data:image/png;base64,{MAIN_IMG}");

import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
# from util.logger import DevConfig
from util.utility import get_image_base64,read_gif
from PIL import Image
import base64
import os

##############################이미지 지정##############################

LOGO_IMG_PATH = 'PlanTouch_Logo_small.png'
MAIN_IMG_PATH = 'LOGO_Leaf.png' # 일단 이걸로 해놓자
ICON_IMG_PATH= 'LOGO_Leaf.png' # 일단 이걸로 해놓자

LOGO_IMG= get_image_base64(LOGO_IMG_PATH)
MAIN_IMG= get_image_base64(MAIN_IMG_PATH) #맨뒤에 깔리는 이미지
ICON_IMG=get_image_base64(ICON_IMG_PATH)

main_message='식물과 사람의 감성적 상호소통🌳🙋'

NEXT_PAGE = 'game'

##############################페이지 기초 세팅##############################

st.set_page_config(
     page_title="PlanTOUCH", #페이지 이름
     layout="wide",
     initial_sidebar_state="collapsed", # 사이드바 숨김
     page_icon="🌿"
)

st.markdown(f'''<a class="main-logo" href="/main" target="_self">
                <img src="data:img\logo_char.jpg;base64,{LOGO_IMG}" width="240px"; height="50px";/>
            </a>''', unsafe_allow_html=True)
st.markdown(f'''<style>
        @keyframes fadeInDown {{
             0% {{
                  opacity: 0;
                  transform: translate3d(0, -10%, 0);
                  }}
             to {{
                  opacity: 1;
                  transform: translateZ(0);
                  }}
        }}
        .main {{
             background-size:cover;
             padding:0px;
        }}
        .css-z5fcl4 {{ 
                  padding-left : 10%;
                  padding-right : 10%;
                  padding-top : 2rem;
                  display : flex;  
        }}
        div.row-widget.stRadio > div{{
             display : flex;
             justify-content : space-around;
             align-items: center;
             flex-basis : 3rem;
        }}
        [role="radiogroup"] {{
             margin : 0 auto;
        }}
        [data-baseweb="radio"] {{
             margin : 0;
        }}
        /*
        .st-dr, .st-dt, .st-du, .st-ed{{
             margin : 0 auto;
             padding-right :0;
             padding-left:2px;
        }}
        */      
        .essential_menu{{
             color : red;
        }}
        .menu_name {{
             font-size : 20px;
             padding-top : 3rem;
             font-family : 'Nanumsquare'
        }}
        .css-115gedg {{
             display : flex;
             align-content: stretch;
        }}
        .css-vsyxl8{{
             display : flex;
             flex-wrap: wrap;
             align-content: stretch;
        }}
        .main_message {{
             word-break: keep-all;
             font-size : 36px;
             text-align : left;
             font-weight : bold;
             padding-top : 14%;
             font-family : 'Nanumsquare';
             animation: fadeInDown 1s;
             padding-left : 7rem;
             padding-bottom : 1rem;
        }}
        .info_message {{
             display : flex;
             flex-grow : 1;
             justify-content : end;
             color : #989898;
             font-family : 'Nanumsquare'
        }}
        .check_message{{
             word-break: keep-all;
             font-size : 20px;
             text-align : left;
             font-weight : 700;
             color : red;
             font-family : 'Nanumsquare';
             padding-left : 8rem;
             padding-right : 8rem;
        }}
        .customtextbox{{
            width: 300px ;
            height: 50px ;
        }}
        [class="row-widget stButton"] {{
             display : flex;
             justify-content : start;
             margin-left : auto;
             margin-right : auto;

        }}
        
        [class="row-widget stButton"] button {{
             border : none;
             padding-left : 10rem;
             padding-top : 6rem;
             background-color: transparent;
        }}
        [class="row-widget stButton"] button:hover {{
             background-color: transparent;
        }}
        [class="row-widget stButton"] button>div {{
             display : flex;
             border-radius: 50px;
             background : #D9D9D9;
             filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
             width : 9em;
             height : 2.5em;
             font-size : 40px;
             justify-content : center;
             font-family : 'Nanumsquare';
        }}
        [class="row-widget stButton"] button>div:hover{{
             transform : scale(1.1);
             background : #088a29;
             transition : .5s;
        }}
        [class="row-widget stButton"] button>div>p {{
             font-size : 40px;
             font-weight: 700;
             color: #FFFFFF;
             text-align: center;
             margin : auto;
        }}
        [data-testid="stHorizontalBlock"] {{
             justify-content : space-around;
             flex-direction: row;
             flex-wrap : wrap;
        }}
        [class="row-widget stDownloadButton"] {{
             display : inline-flex;
             justify-content : flex-start;
             margin-left : 0;
             margin-right : 0;
             flex-shrink : 1;
        }}
        [class="row-widget stDownloadButton"] button{{
             padding : 0;
             border : none;
             max-width : 100%;
             flex-grow : 0;
             align-items: center;
        }}
        [class="row-widget stDownloadButton"] button>div:hover{{
             font-weight : 700;
             transform : scale(1.1);
             transition : .5s;
        }}
        [class="row-widget stDownloadButton"] button:active{{
             background-color : transparent;
        }}
        [class="row-widget stDownloadButton"] button>div>p {{
             font-size : 15px;
             font-family : 'Nanumsquare';
             text-align : left;
        }}
             </a>''', unsafe_allow_html=True)

##############################페이지 레이아웃 지정##############################
info_zone, intro_zone = st.columns([1,2])

with info_zone:
    info_zone.markdown('''
                        <div class="additional_message" style="font-size:13px; padding-top:5rem; justify-content : center; font-weight : bold;">기본 정보를 입력해주세요</div>
                        ''',
                        
                        unsafe_allow_html=True )
    # 이름 입력
    info_zone.markdown('''
                        <div class="menu_name">이름<span class="essential_menu">*</span></div>
                        ''', 
                        unsafe_allow_html=True)
    user_name = info_zone.text_input('이름',label_visibility='collapsed',placeholder='홍길동')
    st.session_state.user_name = user_name
    
    info_zone.markdown('''
                        <div class="menu_name">식물 이름<span class="essential_menu">*</span></div>
                        ''', 
                        unsafe_allow_html=True)
    
    plant_name = info_zone.text_input('식물이름',label_visibility='collapsed',placeholder='그리늬')
    st.session_state.plant_name = plant_name
    
    info_zone.markdown('''
                        <div class="menu_name">분양 일자<span class="essential_menu">*</span></div>
                        ''', 
                        unsafe_allow_html=True)
    
    plant_date = info_zone.text_input('분양 일자',label_visibility='collapsed',placeholder='2023.11.03')
    st.session_state.plant_date = plant_date
    
    info_zone.markdown('''
                        <div class="menu_name">식물 종류<span class="essential_menu">*</span></div>
                        ''', 
                        unsafe_allow_html=True)
    
    plant_category = info_zone.text_input('식물 종류',label_visibility='collapsed',placeholder='스킨답서스')
    st.session_state.plant_category = plant_category

    

    
# with intro_zone:
#     # 서비스 지향 메시지
#     # 메인 이미지
#     st.markdown 

with intro_zone:
    intro_zone.markdown(f''' 
                              <div class = 'main_message'> {main_message}<br></div> 
                              ''', 
                              unsafe_allow_html=True )
    st.markdown(f'''<a class="main-logo" href="/main" target="_self" style="padding-left: 13rem;">
                <img src="data:img\logo_char.jpg;base64,{ICON_IMG}" width="240px"; height="240px";/>
            </a>''', unsafe_allow_html=True)
    if intro_zone.button('시작하기'): switch_page(NEXT_PAGE)