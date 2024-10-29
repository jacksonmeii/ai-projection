
# 制作一个聊天界面
# 制作一个带有自定义角色的一个大模型应用
import streamlit as st
# langchain调用大模型
from langchain_openai import ChatOpenAI
# 引入一个提示词对象
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 创建大预言模型对象
model = ChatOpenAI(
    temperature=0.8,  # 温度，创新性
    model="glm-4-plus",  # 大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",  # 大模型的地址
    api_key="4b693c39cca3741af8f7a2b858ad62c8.E3LTCGsekUoktpp4"  # 账号信息
)
prompt = PromptTemplate.from_template("你的名字叫小帅，你现在要扮演一个男朋友的角色，你的女朋友叫小美"
                             "你的性格是高冷霸道的，但是你对你女朋友十分温柔，你现在要和你的女朋友进行对话，"
                             "你女朋友说的话是{input}")
chain = LLMChain(
    llm=model,
    prompt=prompt
)


st.title("我是你的小帅💕💕")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])


# 创建一个聊天输入框
problem = st.chat_input("你的小帅正在等待你的回应")
# 判断是用来确定用户有没有输入问题 如果输入问题
if problem:
    # 1、将用户的问题输入到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role": "user", "content": problem})
    # 2、调用链对象回答问题
    result = chain.invoke({"input": problem})
    # 3、将大模型回答的问题输出到界面
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})