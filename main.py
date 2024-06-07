import streamlit as st
from utils import generate_script

st.title("🎬 视频脚本生成器")

with st.sidebar:
    tongyi_api_key=st.text_input("请输入通义千问的API密钥:",type="password")
    st.markdown("[获取通义千问的API密钥](https://dashscope.console.aliyun.com/apiKey)")

subject=st.text_input("💡 请输入视频的主题")
video_length=st.number_input("⏱️ 请输入视频的大致时长（单位：分钟）",min_value=0.1,step=0.1)
creativity=st.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit=st.button("生成脚本")

if submit and not tongyi_api_key:
    st.info("请输入你的通义千问API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length>=0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):
        title,script = generate_script(subject,video_length,creativity,tongyi_api_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题:")
    st.write(title)
    st.subheader("📝 视频脚本:")
    st.write(script)
