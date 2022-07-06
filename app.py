import streamlit as st
# import requests

st.title("Voight Kampff")
st.image("https://m.economictimes.com/thumb/msid-66752021,width-1200,height-900,resizemode-4,imgsize-98420/robot-touch.jpg")
st.markdown(":performing_arts:Rules: you will be randomly assign ai :vs: human role, click play if you are ready.", unsafe_allow_html=False)

start = st.button("Play")
if start:
    st.balloons()
    st.write("game start")
    # request=requests.get(url).json()
    # # message=request[0]
    st.success("here is the message for you")
    with st.expander("check message"):
        st.write("""message1
             """)
    st.success("let's fool them")
