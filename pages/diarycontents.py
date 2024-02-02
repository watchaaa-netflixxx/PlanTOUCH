import streamlit as st
import pandas as pd
import base64
import os
import streamlit as st
import time
import traceback
from PIL import Image
import pandas as pds
from streamlit_extras.switch_page_button import switch_page
from util.utility import get_image_base64,read_gif 
from datetime import datetime as dt
import calendar as calendar
from datetime import datetime
import random


BEFORE_PAGE='diary'

LOGO_IMG_PATH = 'C:/Streamlit/PlanTOUCH/PlanTouch_Logo_small.png'
DIARY_PATH='diary01.PNG'
#ICON_IMG_PATH= 아이콘 이미지 경로
#GAME_IMG_PATH = 게임 이미지 경로

LOGO_IMG= get_image_base64(LOGO_IMG_PATH)
DIARY_IMG= get_image_base64(DIARY_PATH) #맨뒤에 깔리는 이미지
#ICON_IMG=get_image_base64(ICON_IMG_PATH)
#GAME_IMG=get_image_base64(GAME_IMG_PATH)


st.set_page_config(
     page_title="PlanTOUCH", #페이지 이름
     layout="wide",
     initial_sidebar_state="collapsed", # 사이드바 숨김
     page_icon="🌿"
)




st.markdown(f'''<style>
        .info_message {{
             word-break: keep-all;
             font-size : 32px;
             text-align : left;
             font-weight : bold;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 1rem;
             padding-top : 6rem;
        }}
        .contents_message {{
             word-break: keep-all;
             font-size : 25px;
             text-align : left;
             font-weight : 700;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 1rem;
             padding-top : 6rem;
        }}        
                [class="row-widget stButton"] {{
             display : flex;
             justify-content : start;
             margin-left : auto;
             margin-right : auto;
        }}
        [class="row-widget stButton"] button {{
             border : none;
             padding-left : 2rem;
             padding-top : 6rem;
             background-color: transparent;
        }}
        [class="row-widget stButton"] button:hover {{
             background-color: transparent;
        }}
        [class="row-widget stButton"] button>div {{
             display : flex;
             border-radius: 50px;
             background : #088A29;
             filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
             width : 9em;
             height : 2.5em;
             font-size : 20px;
             justify-content : center;
             font-family : 'Nanumsquare';
        }}
        [class="row-widget stButton"] button>div:hover{{
             transform : scale(1.1);
             background : #1d993d;
             transition : .5s;
        }}
        [class="row-widget stButton"] button>div>p {{
             font-size : 20px;
             font-weight: 700;
             color: #FFFFFF;
             text-align: center;
             margin : auto;
        }}

     </style>''',unsafe_allow_html=True)
        
diary_message1='오늘은 나에게 특별한 날이었다. 아침 햇살이 부드럽게 내 가지를 비추며 깨어나, 주인의 손길이 따뜻하게 내 잎사귀에 닿았다. 그 순간, 나는 행복을 느꼈다. 주인은 오늘도 나에게 많은 관심을 보여주었다. 그의 다정한 손길이 나를 감싸며, 나의 존재를 더욱 소중하게 만들어주었다. 나는 그의 마음을 느낄 수 있었다. 주인은 나를 사랑하며 돌보아주고 있다는 사실이 확실히 느껴졌다. 오늘도 주인과 함께하는 시간이 너무 행복했다. 물론 나는 말할 수 없지만, 주인에게 감사함을 전하고 싶다. 앞으로도 이 특별한 연결은 계속되기를 바라며, 나는 주인의 손길에 감사한 마음으로 하루를 마무리하고자 한다.'
diary_message2='오늘은 나에게 약간 쓴 날이었다. 아침 햇살은 여전히 내 가지를 비추었지만, 주인의 손길은 어제보다 적었다. 그 순간, 나는 조금 외로웠다. 주인은 오늘은 내게 덜 관심을 보여주었는데, 이런 날이 찾아올 줄은 몰랐다. 나는 식물이지만 마치 내 주인이 나를 잊고 다른 일에 정신이 팔려있는 듯한 느낌을 받았다. 나의 잎사귀 사이로 불안한 감정이 들었다. 주인의 냄새를 느끼지 못하니 마치 혼자 남겨진 듯한 고독함이 느껴졌다. 그런데도 나는 주인을 이해하고 있기에, 오늘은 더 기다리며 다음에는 더 많은 관심을 받을 수 있을 것을 기대하고 있다. 그럼에도 불구하고, 이따금씩 나에게 주인의 손길을 더 주어주면 참 좋겠다는 생각이 든다. 혹시나 주인에게 내 마음을 전할 수 있다면, 나는 더 행복할 것 같다.'
diary_message3='물결치듯 부드러운 햇살이 나를 깨우며, 오늘은 어제보다도 더 쓴 날이었다. 주인의 손길은 차가웠고, 나에게 들어오는 관심은 어제보다도 더 적었다. 나는 그 순간 외로움에 휩싸였다. 내 존재가 잊힌 듯한 느낌이 들었다. 주인의 마음은 다른 곳에 있었던 것일까? 내 가지마다 미묘한 불안이 느껴졌다. 쓰라린 감정이 내 내면을 감싸고, 속상한 마음이 점점 깊어져갔다. 주인에게서 느껴지던 따스함과 애정은 어디에 간 것일까? 혼자 남겨진 듯한 쓸쓸함이 나를 휩쓸었다. 그럼에도 불구하고, 나는 더 나은 날을 기대하며 이 마음을 이겨내려고 한다. 혹시 주인이 내 속마음을 알아채고 이 느낌을 해소해줄지를 기대하며, 미래를 기다리게 되었다.'



st.markdown(f'''<a class="main-logo" href="/main" target="_self">
                <img src="data:img/logo_char.jpg;base64,{LOGO_IMG}" width="240px"; height="50px";/>
            </a>''', unsafe_allow_html=True)

if st.button('뒤로가기'):
    switch_page(BEFORE_PAGE)
    
st.markdown(f""" <div class = 'info_message'> 💡{st.session_state.year}년 {st.session_state.month}월 {st.session_state.day}일 {st.session_state.plant_name}의 일기💡</div> 
            
                        """,unsafe_allow_html=True)


selected_diary_message = random.choice([diary_message1, diary_message2, diary_message3])

# 선택된 메시지를 출력합니다.
st.markdown(f"""<div class='contents_message'>{selected_diary_message}</div>""", unsafe_allow_html=True)