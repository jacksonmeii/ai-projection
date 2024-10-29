from zhipuai import ZhipuAI
import streamlit as st

model = ZhipuAI(api_key="4b693c39cca3741af8f7a2b858ad62c8.E3LTCGsekUoktpp4")

st.title("设计")

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] == 'user':
            with st.chat_message(message['role']):
                st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"], width=300)



desc = st.chat_input("请输入图片的描述")
if desc:
    with st.chat_message("user"):
        st.write(desc)
        st.session_state.cache.append({"role":"user","content":desc})
    response = model.images.generations(
            model="cogview-3-plus",  # 填写需要调用的模型编码
            prompt=desc,
        )

    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=300)
    st.session_state.cache.append({"role":"assistant","content":response.data[0].url})