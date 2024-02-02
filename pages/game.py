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
import json

##############################이미지 지정##############################

LOGO_IMG_PATH = 'C:/Streamlit/PlanTOUCH/PlanTouch_Logo_small.png'
MAIN_IMG_PATH = 'C:/Streamlit/PlanTOUCH/LOGO_Leaf.png' # 일단 이걸로 해놓자
#ICON_IMG_PATH= 아이콘 이미지 경로
#GAME_IMG_PATH = 게임 이미지 경로

LOGO_IMG= get_image_base64(LOGO_IMG_PATH)
MAIN_IMG= get_image_base64(MAIN_IMG_PATH) #맨뒤에 깔리는 이미지
#ICON_IMG=get_image_base64(ICON_IMG_PATH)
#GAME_IMG=get_image_base64(GAME_IMG_PATH)

FLOWER_GIF1= read_gif('C:/Streamlit/PlanTOUCH/HappyMotionNormal.gif')
FLOWER_GIF0= read_gif('C:/Streamlit/PlanTOUCH/HappyMotion_Blooming_Orange.gif')
FLOWER_GIF2 = read_gif('C:/Streamlit/PlanTOUCH/HappyMotion_Wave.gif')
FLOWER_GIF3 = read_gif('C:/Streamlit/PlanTOUCH/HappyMotion_round2.gif')


main_message = "Plant-다마고치,"
sub_message="Touch를 통한 성장"
message="실제 식물에 터치하는 방식에 따라,<br>게이지가 증가하고 식물이 성장합니다. "

NEXT_PAGE1='diary'
NEXT_PAGE2='mypage'

##############################페이지 기초 세팅##############################

st.set_page_config(
     page_title="PlanTOUCH", #페이지 이름
     layout="wide",
     initial_sidebar_state="collapsed", # 사이드바 숨김
     page_icon="🌿"
)

st.markdown(f'''<a class="main-logo" href="/main" target="_self">
                <img src="data:img/logo_char.jpg;base64,{LOGO_IMG}" width="240px"; height="50px";/>
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
        .game-zone {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
        }}
        .main_message {{
             word-break: keep-all;
             font-size : 36px;
             text-align : left;
             font-weight : bolder;
             padding-top : 14%;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 7rem;

        }}
        .info_message {{
             word-break: keep-all;
             font-size : 32px;
             text-align : left;
             font-weight : normal;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 15rem;
             padding-bottom : 5rem;
        }}
        .sub_message {{
             word-break: keep-all;
             font-size : 32px;
             text-align : left;
             font-weight : normal;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 7rem;
             padding-bottom : 1rem;
        }}       
        .message {{
             word-break: keep-all;
             font-size : 20px;
             text-align : left;
             font-weight : normal;
             font-family : 'Nanumsquare';
             animation: fadeInDown 2s;
             padding-left : 7rem;
             padding-bottom : 1rem;
        }}     
        .addmessage{{
             word-break: keep-all;
             font-size : 26px;
             padding-left : 3rem;
             text-align : left;
             font-weight : bold;
             font-family : 'Nanumsquare';
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
        .meter {{
             box-sizing: content-box;
             width: 800px;
             height: 20px; 
             position: relative ;
             margin: 50px 0 20px 0;
             background: #555;
             border-radius: 25px;
             padding: 10px;
             box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.3);
             }}
        .meter > span {{
              display: block;
              height: 100%;
              border-top-right-radius: 8px;
              border-bottom-right-radius: 8px;
              border-top-left-radius: 20px;
              border-bottom-left-radius: 20px;  
              background-color: rgb(43, 194, 83);
              background-image: linear-gradient(
                   center bottom,
                   rgb(43, 194, 83) 37%,
                   rgb(84, 240, 84) 69%
                   );
               box-shadow: inset 0 2px 9px rgba(255, 255, 255, 0.3),
               inset 0 -2px 6px rgba(0, 0, 0, 0.4);
               position: relative;
               overflow: hidden;
               }}
               
          .meter > span:after,
          .nostripes > span > span,
          
          .nostripes > span::after {{background-image: none;}}
          .green > span {{background-image: linear-gradient(#c3d9c9, #1d993d);}}        
          .green2 > span {{ baground_image: linear-gradient (#c3d9c9,#6ba30a);}}
          .green3 > span {{ baground_image: linear-gradient (#709fd4,#0b70e3);}}
     </style>''',unsafe_allow_html=True)
 
 
##############################게이지바 만들어주기##############################       
# Your min and max values
min_val = 0
max_val = 100  # 100 iterations for simplicity

# Create a placeholder for the progress bar and text

current_val=80
    
percentage = current_val / max_val

show_gif = True


##############################페이지 레이아웃 세팅##############################

menu_form, game_zone = st.columns([1,2])

###############################메뉴 부분 세팅##############################
with menu_form:
     menu_form.markdown(f"""
                              <div class = 'main_message'> {main_message}</div> 
                              <div class = 'sub_message'> {sub_message}<br></div>
                              <div class = 'message'> {message}<br></div>
                              <p style="padding-left : 10rem;">
                              """, 
                              unsafe_allow_html=True )


     
     if menu_form.button('식물 일기🗓️'): switch_page(NEXT_PAGE1)
     elif menu_form.button('마이페이지🏡'): switch_page(NEXT_PAGE2)
     if menu_form.button("LEVEL UP"):show_gif = not show_gif
current_gif = FLOWER_GIF1 if show_gif else FLOWER_GIF0

d=24

##############################게임부분 세팅##############################
with game_zone:   
     game_zone.markdown(f""" <div class = 'info_message'> '{st.session_state.user_name}'님의 '{st.session_state.plant_name}🍀'</div> 
                        """,unsafe_allow_html=True)
     game_zone.markdown(f"""  <p style=  "padding-left : 18rem";>
                              <img src="data:img/logo_char.jpg;base64,{current_gif}"  width="350px"; height="350px";/><p/>
                              """, 
                              unsafe_allow_html=True )
     label = '🌻🌼전체 게이지 : '
     label1 =  d 
     label2 = ' %🌻🌼'
     
     st.markdown(f'''
                 <div class = 'addmessage'> {label}{label1}{label2}</div> 
                 ''', unsafe_allow_html=True)      

# CSS 스타일 동적 생성
progress_bar_style = f'''
    <style>
        .meter-container {{
            display: flex;
            align-items: center;
            margin-bottom: 4rem;
        }}
        .meter-container2 {{
            display: flex;
            align-items: center;
            margin-bottom: 8rem;
        }}
        .text-container {{
            margin-left: 30rem;
            padding-top : 3rem;
            position: fixed; 
        }}
        .meter {{
            box-sizing: content-box;
            width: 800px;
            height: 20px;
            margin: 65px 0 40px 34rem;
            position: fixed; 
            background: #555;
            border-radius: 25px;
            padding: 10px;
            box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.3);
        }}
        .meter > span {{
            display: block;
            height: 100%;
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            background-color: rgb(43, 194, 83);
            background-image: linear-gradient(
                center bottom,
                rgb(43, 194, 83) 37%,
                rgb(84, 240, 84) 69%
            );
            box-shadow: inset 0 2px 9px rgba(255, 255, 255, 0.3),
                        inset 0 -2px 6px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
        }}
        .meter > span:after,
        .nostripes > span > span,
        .nostripes > span::after {{
            background-image: none;
        }}
        .green > span {{
            background-image: linear-gradient(#c3d9c9, #1d993d);
        }}
        .green2 > span {{
            background-image: linear-gradient(#c3d9c9, #6ba30a);
        }}
        .green3 > span {{
            background-image: linear-gradient(#709fd4, #0b70e3);
        }}
        .text-large {{
            font-size: 30px;  /* Adjust the font size as needed */
        }}
    </style>
'''

# 현재값을 최소값과 최대값 사이의 비율로 변환
percentage0 = 0.4
percentage1 = 0.0
percentage2 = 0.65
# current_val / max_val

with open('class_dict.json', 'r') as f:
    data = json.load(f)
    label0=data['class_result']

print("JSON 파일에서 읽은 데이터: ", data['class_result'])

label0=data['class_result']
# st.markdown(f'''
#                  <div class = 'addmessage'> {label0}</div> 
#                  ''', unsafe_allow_html=True)

if data['class_result']==0:
    percentage0+=0.5 
elif data['class_result']==1:
    percentage1+=0.5
elif data['class_result']==2:
    percentage2+=0.5



# HTML로 표시
st.markdown(progress_bar_style, unsafe_allow_html=True)
st.markdown(f'''
    <div class="meter-container">
        <div class="text-container text-large">
            <span>🖐</span>
        </div>
    <div class="meter green2 nostripes">
        <span style="width: {percentage0 * 100}%"></span>
    </div>
''', unsafe_allow_html=True)

st.markdown(progress_bar_style, unsafe_allow_html=True)
st.markdown(f'''
    <div class="meter-container">
        <div class="text-container text-large">
            <span>✌</span>
        </div>
    <div class="meter green2 nostripes">ff
        <span style="width: {percentage1 * 100}%"></span>
    </div>
''', unsafe_allow_html=True)

st.markdown(progress_bar_style, unsafe_allow_html=True)
st.markdown(f'''
    <div class="meter-container2">
        <div class="text-container text-large">
            <span>👋</span>
        </div>
    <div class="meter green2 nostripes">
        <span style="width: {percentage2 * 100}%"></span>
    </div>
''', unsafe_allow_html=True)

b = "무슨 일 있으신가요?"
c = "감사합니다"
d = "고맙습니다"
e = ".........."

a=st.empty()

while(True):

    with open('class_dict.json', 'r') as f:
        class_data = json.load(f)
          
    if class_data['class_result'] == 0:
        
        a.write(b)

        class_data = {"class_result" : 4}
                        
        with open('class_dict.json','w') as f:
            json.dump(class_data, f)

    elif class_data['class_result'] == 1:
        
        a.write(c)

        class_data = {"class_result" : 4}
                        
        with open('class_dict.json','w') as f:
            json.dump(class_data, f)

    elif class_data['class_result'] == 2:
        
        a.write(d)

        class_data = {"class_result" : 4}
                        
        with open('class_dict.json','w') as f:
            json.dump(class_data, f)

    else:
        a.write(e)

    time.sleep(3)
