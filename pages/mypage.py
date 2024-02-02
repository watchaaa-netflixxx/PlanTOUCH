
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

LOGO_IMG_PATH = 'PlanTouch_Logo_small.png'

LOGO_IMG= get_image_base64(LOGO_IMG_PATH)

#ICON_IMG=get_image_base64(ICON_IMG_PATH)
#GAME_IMG=get_image_base64(GAME_IMG_PATH)


st.set_page_config(
     page_title="PlanTOUCH", #페이지 이름
     layout="wide",
     initial_sidebar_state="collapsed", # 사이드바 숨김
     page_icon="🌿"
)

st.markdown(f'''<a class="main-logo" href="/main" target="_self">
                <img src="data:img\logo_char.jpg;base64,{LOGO_IMG}" width="240px"; height="50px";/>
            </a>''', unsafe_allow_html=True)
# st.markdown(f'''<style>
#         .main {{
#              background-size:contain;
#              background-image: url("data:image/png;base64,{MyPage_IMG}");
#              background-repeat: no-repeat;
#              padding:0px;
#              background-position: center center;
#              position: fixed;
#         }}
#         .info_plantname {{
#              word-break: keep-all;
#              font-size : 32px;
#              text-align : left;
#              font-weight : bold;
#              font-family : 'Nanumsquare';
#              animation: fadeInDown 2s;
#              padding-left : 72rem;
#              padding-top : 8rem;}}
#         .info_plantkind {{
#              word-break: keep-all;
#              font-size : 32px;
#              text-align : left;
#              font-weight : bold;
#              font-family : 'Nanumsquare';
#              animation: fadeInDown 2s;
#              padding-left : 64rem;
#              padding-top : 18rem;}}       
#         .info_plantdate {{
#              word-break: keep-all;
#              font-size : 32px;
#              text-align : left;
#              font-weight : bold;
#              font-family : 'Nanumsquare';
#              animation: fadeInDown 2s;
#              padding-left : 64rem;
#              padding-top : 16rem;}}     
#         .info_username {{
#              word-break: keep-all;
#              font-size : 32px;
#              text-align : left;
#              font-weight : bold;
#              font-family : 'Nanumsquare';
#              animation: fadeInDown 2s;
#              padding-left : 64rem;
#              padding-top : 16rem;}} 
#           </a>''', unsafe_allow_html=True)


# st.markdown(f""" <div class = 'info_plantname'> 💡{st.session_state.plant_name} </div> 
            
#                         """,unsafe_allow_html=True)

# st.markdown(f""" <div class = 'info_plantkind'> 💡{st.session_state.plant_category} </div> 
            
#                         """,unsafe_allow_html=True)

# # st.markdown(f""" <div class = 'info_plantdate'> 💡{st.session_state.plant_date} </div> 
            
# #                         """,unsafe_allow_html=True)

# # st.markdown(f""" <div class = 'info_username'> 💡{st.session_state.use_name} </div> 
            
# #                         """,unsafe_allow_html=True)
# 스타일 정의
# container_style = """
#     border-width: 2px;
#     border-style: solid;
#     border-color: blue;
#     padding: 20px;
#     border-radius: 10px;
# """

# # 네모 카드 안에 텍스트 넣기
# with st.container():
#     st.title("네모 카드 안에 텍스트")

#     # 컨테이너에 스타일 적용
#     st.markdown(f'<div style="{container_style}">', unsafe_allow_html=True)

#     # 카드의 내용
#     st.markdown("""
#     이곳에는 텍스트를 넣을 수 있습니다.
    
#     여러 줄의 텍스트도 작성할 수 있습니다.
    
#     - 리스트 항목 1
#     - 리스트 항목 2
#     - 리스트 항목 3
#     """)

#     # 카드 하단에 버튼 추가
#     if st.button("버튼을 눌러보세요"):
#         st.write("버튼이 눌렸습니다!")

#     # 컨테이너 닫기