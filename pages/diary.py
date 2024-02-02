# # 달력 만들기
# # 각자 버튼 연결 => key 마다 새로운 페이지로 연결?
# # GPT API 연결 하기

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

LOGO_IMG_PATH = 'C:/Streamlit/PlanTOUCH/PlanTouch_Logo_small.png'
MAIN_IMG_PATH = 'C:/Streamlit/PlanTOUCH/LOGO_Leaf.png' # 일단 이걸로 해놓자
#ICON_IMG_PATH= 아이콘 이미지 경로
#GAME_IMG_PATH = 게임 이미지 경로

LOGO_IMG= get_image_base64(LOGO_IMG_PATH)
MAIN_IMG= get_image_base64(MAIN_IMG_PATH) #맨뒤에 깔리는 이미지
#ICON_IMG=get_image_base64(ICON_IMG_PATH)
#GAME_IMG=get_image_base64(GAME_IMG_PATH)

CONTENT_PAGE='diarycontents'

st.set_page_config(
     page_title="PlanTOUCH", #페이지 이름
     layout="wide",
     initial_sidebar_state="collapsed", # 사이드바 숨김
     page_icon="🌿"
)

st.markdown(f'''<a class="main-logo" href="/main" target="_self">
                <img src="data:img/logo_char.jpg;base64,{LOGO_IMG}" width="240px"; height="50px";/>
            </a>''', unsafe_allow_html=True)
current_year = datetime.now().year
current_month = datetime.now().month
st.markdown(
    """
    <style>
        .selectbox-container {
            padding-top: 10px;  /* 원하는 패딩 값으로 조정 */
        }
        .selectbox label {
            font-size: 20px;  
        }
    </style>
    """,
    unsafe_allow_html=True
)
# 년도와 월을 선택하는 셀렉트 박스
cyr = st.selectbox("년도", list(range(current_year - 5, current_year + 6)), index=5)
cmnt = st.selectbox("월", list(range(1, 13)), index=current_month - 1)


myclndr = calendar.monthcalendar(cyr, cmnt)

wk1 = myclndr[0]
wk2=myclndr[1]
wk3=myclndr[2]
wk4=myclndr[3]
wk5=myclndr[4]
html_str_a = ""
html_str_b = "<br><br>"
     
background_color = "#e0efe4" 
st.markdown(f"""  <style>
            .info_message {{
             word-break: keep-all;
             font-size : 32px;
             text-align : left;
             font-weight : bold;
             font-family : 'Nanumsquare';
             background-color: {background_color};
             animation: fadeInDown 2s;

        }} """,unsafe_allow_html=True)

label=cyr
label1='년'
label2=cmnt
label3='월'     
st.markdown(f'''
            <div class = 'info_message'> {label}{label1}{label2}{label3}  <'{st.session_state.plant_name}'의 일기🌳📚></div> 
            ''', unsafe_allow_html=True)    
cols = st.columns(7)
i=0

empty_days_count = 0
button_states = {} 
for week_num, week in enumerate([wk1, wk2, wk3, wk4, wk5]):
    for vday in week:
        if vday > 0:
            # 비어 있는 날짜의 개수를 고려하여 인덱스 조정
            adjusted_index = vday - (empty_days_count + 7 * week_num + 1)
            cols[adjusted_index].markdown("<hr style='border-top: 1px solid #ddd'>", unsafe_allow_html=True)
            cols[adjusted_index].markdown(html_str_a + str(vday).zfill(2) + html_str_b, unsafe_allow_html=True)
            # cols[adjusted_index].button("🗓️", key=f"DY{vday}")
            button_key = f"DY{vday}"
            
            # 각 버튼에 대한 상태를 저장
            button_states[button_key] = cols[adjusted_index].button("🗓️", key=button_key)
            
            # 해당 버튼이 클릭되었는지 확인
            if button_states[button_key]:
                st.session_state.year=cyr
                st.session_state.month = cmnt
                st.session_state.day = vday
                switch_page(CONTENT_PAGE)
            
        else:
            # 비어 있는 날짜는 공백으로 표시
            # cols[i].markdown("        ", unsafe_allow_html=True)
            i += 1
            
button_clicked = cols[adjusted_index].button("🗓️", key=f"DY{vday}")   
if button_clicked:
        st.write(f"Button for {vday} was clicked!")
        
        
st.markdown("""
            <style>div[data-testid="stVerticalBlock"] div[data-testid="stMarkdownContainer"] p {
                text-align: center;}
                </style>""",unsafe_allow_html=True)

