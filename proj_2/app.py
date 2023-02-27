import streamlit as st

st.title("Innomatics Data App")
st.title("SANJEEVANI")
st.snow()

st.subheader("Passionate about data and in a journey to drill deep into data science and would love to connect people interested in data:smile::smile:")

st.header("Connect with me")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()