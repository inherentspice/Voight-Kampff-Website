from cmath import isnan
from curses.ascii import isblank
from types import resolve_bases
from typing import Container
import streamlit as st
import requests
import random
import streamlit_modal as modal
import streamlit.components.v1 as components
import datetime

url = "https://vktest-kr575za6oa-uw.a.run.app/response?"
payload_url = "https://vktest-kr575za6oa-uw.a.run.app/question"
payload_response = requests.get(payload_url).json()
payload = {"question": payload_response.get('question')}

#game title#
st.title(":video_game: Voight Kampff :video_game:    :robot_face::vs::face_with_rolling_eyes: ")
check_rule = st.button("Game Rules")

user_name = ['apple','orange','pear','pie','turkey','burger','sandwich','water','coke','pepsico']
room = (1001)
players = (6)
player_name= random.choice(user_name)
col1, col2, col3 = st.columns(3)
col1.metric("Room", room, "4 online")
col2.metric("players number", players)
col3.metric("Player name", player_name)

st.image("https://m.economictimes.com/thumb/msid-66752021,width-1200,height-900,resizemode-4,imgsize-98420/robot-touch.jpg")

if check_rule:
    modal.open()
    # browser_console_log('Opening the model')

if modal.is_open():
    # browser_console_log('model is opened')
    with modal.container():
        # browser_console_log('Inside the container')
        st.write("Game Rules")
        # st.image("https://m.economictimes.com/thumb/msid-66752021,width-1200,height-900,resizemode-4,imgsize-98420/robot-touch.jpg")
        st.markdown("""
            ### :performing_arts: Rules: you will be randomly assign :robot_face:AI:vs: :face_with_rolling_eyes: Human role.

            ### :game_die: Players are secretly divided into two teams – humans and :robot_face:androids.

            ### :face_with_rolling_eyes: Humans answer :question: questions and then share them with the group.

            ### :robot_face: Androids are :eye: provided answers generated by a Deep Learning :rocket: model and must convince the group they are human.:performing_arts:

            ### :speech_balloon: Players have time to discuss and vote each other out.Users might all be human. They might all be androids. Each game is random.

            """, unsafe_allow_html=False)
        checked = st.checkbox("Okay, got it.")
        if checked is True:
            modal.close()
        # st.write(f"Checkbox checked: {value}")

open_room = st.button('Get a game room')
if open_room:
    with st.container():
        room_select = st.radio(
            "Would you like o creat a game room or join a game room?",
            ('New room', 'join a room'))
        if room_select == 'New room':
            room = random.randint(1000,9999)
            st.write('Your room number is', room,'!')
        if room_select == 'join a room':
            room = st.number_input('please enter the room number',min_value=1000,max_value=9999)
            st.write('You select the', room,'!')
        go2room = st.checkbox("Okay, take me to the room.")
        if go2room is True:
            Container.close()

# # def browser_console_log(msg:str):
# #     components.html(f'<script>console.log("{msg}")</script>')

question= str(payload_response.get('question'))
answer = requests.get(url, params=payload).json()
ai_answer= answer.get('response')

# # # browser_console_log('Start playing the play button')
start = st.button("Play")
st.spinner("please wait, retrieving the message!")
role =[]
if start:
    start = datetime.datetime.now()
    roles =random.choice(["AI","Human"])
    role = roles
    if start and role =="AI":
        st.spinner("please wait, retrieving the message!")
        ai_answer= answer.get('response')
        st.markdown("""
                    #Your role is AI
                    """, unsafe_allow_html=False)
        st.write('Question?',question,)
        st.write('Your answer is:', ai_answer,'!')
        st.snow()
        end = datetime.datetime.now()
        diff = end - start
        print(f'How long does it take to get Q&A for AI: {diff}')
    elif start and role == "Human":
        st.spinner("please wait, retrieving the message!")
        st.balloons()
        st.write('Your role is human')
        st.write("Question:", question)
        end = datetime.datetime.now()
        diff = end - start
        print(f'How long does it take to get question for human: {diff}')
answer_box = st.text_input('answer box',placeholder='type your answer')
st.write('Question?',question,'?','Your answer is:', answer_box,'!')

# ##########################
# # #assign random role to user
# # #assign message to user
# # #create user
# # #######################

print('\n'*2,'-'*30)
print(f'My role is: {role}')

# # ########
# # #game rules
# # ########

# # # # process-1 assign message and role
# # # payload_response = requests.get(payload_url).json()
# # # payload = {"question": payload_response.get('question')}
# # # browser_console_log(payload_response.get('question'))
# # # answer = requests.get(url, params=payload).json()
# # # ai_answer= answer.get('response')
# # # browser_console_log(ai_answer)
# #     # st.success("let's fool them")
# # @st.experimental_memo
# # def qa(question):
# #     if role == "AI":
# #         ai_answer= answer.get('response')
# #         return ai_answer
# #     if role == "Human":
# #         answerbox = st.text_input(question, 'type here')
# #         st.write(question,answerbox)
# # # #display other user
# # # #make selection

# option = st.selectbox( 'What do you think player B is?',('AI', 'Human'))
# st.write('You selected:', option)
guess = st.select_slider(
     'Select a role you guess player b is',
     options=['AI', 'Human'])
st.write('My guess is', guess)

# # # #announce the asnwer- picture+userid+roles
reveal= st.button("reveal")
if reveal:
    IMAGE_PATH = '/Desktop/'
    img_file = st.camera_input("Take a picture")
    # st.write("winner is",img_file)
    # with open(IMAGE_PATH, 'rd'):
        # pass

# # #         # answer = requests.get(url, params=payload).json()
# # #         # ai_answer1 = answer.get('response')
# # #         # question1 = str(payload_response.get('question'))
# # #         # givenanswer= ai_answer.rpartition('?')[2]
