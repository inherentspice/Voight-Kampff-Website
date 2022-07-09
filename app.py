import streamlit as st
import requests

IMAGE_PATH = '/Desktop/'

#game introduction#
st.title(":video_game: Voight Kampff :video_game:    :robot_face::vs::face_with_rolling_eyes: ")
st.image("https://m.economictimes.com/thumb/msid-66752021,width-1200,height-900,resizemode-4,imgsize-98420/robot-touch.jpg")
st.markdown("""
            # :performing_arts: Rules: you will be randomly assign :robot_face:AI:vs: :face_with_rolling_eyes: Human role.

            ### :game_die: Players are secretly divided into two teams – humans and :robot_face:androids.

            ### :face_with_rolling_eyes: Humans answer :question: questions and then share them with the group.

            ### :robot_face: Androids are :eye: provided answers generated by a Deep Learning :rocket: model and must convince the group they are human.:performing_arts:

            ### :speech_balloon: Players have time to discuss and vote each other out.Users might all be human. They might all be androids. Each game is random.

            #click play if you are ready

            """, unsafe_allow_html=False)

# rule=

#create user
# process-1 assign message and role
start = st.button("Play")
if start:
    st.balloons()
    url = "https://vktest-kr575za6oa-uw.a.run.app/response?"
    payload_url = "https://vktest-kr575za6oa-uw.a.run.app/question"
    payload_response = requests.get(payload_url).json()
    payload = {"question": payload_response.get('question')}
    answer = requests.get(url, params=payload).json()
    ai_answer = answer.get('response')
    # st.write({ai_answer})
    # request=requests.get(url).json()
    # # message=request[0]
    st.success("here is the message for you")
    with st.expander("check message"):
        st.title(ai_answer)
    st.success("let's fool them")

#assign random role to user
#assign message to user
#display other user
#make selection


option = st.selectbox( 'what do you think player B is?',('AI', 'Human'))
st.write('You selected:', option)

#announce the asnwer- picture+userid+roles
reveal= st.button("reveal")
if reveal:
    img_file = st.camera_input("Take a picture")
    # st.write("winner is",img_file)
    with open(IMAGE_PATH, 'rd'):
        pass
