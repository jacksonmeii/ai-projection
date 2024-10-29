# 制作一个聊天界面
import streamlit as st
# langchain调用大模型
from langchain_openai import ChatOpenAI

# 构建一个大模型--智普AI
model = ChatOpenAI(
    temperature=0.8,  # 温度，创新性
    model="glm-4-plus",  # 大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",  # 大模型的地址
    api_key="4b693c39cca3741af8f7a2b858ad62c8.E3LTCGsekUoktpp4"  # 账号信息
)

st.title("AI demo小程序😍😍")
# 创建一个聊天输入框
problem = st.chat_input("请输入你的问题")
# 判断是用来确定用户有没有输入问题 如果输入问题
if problem:
    # 1、将用户的问题输入到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    #2、调用大模型回答问题
    result = model.invoke(problem)
    #3、将大模型回答的问题输出到界面
    with st.chat_message("assistant"):
        st.write(result.content)