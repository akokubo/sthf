import streamlit as st
import requests

# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
# API_URL = "https://api-inference.huggingface.co/models/rinna/japanese-gpt2-small"
API_URL = "https://api-inference.huggingface.co/models/cyberagent/open-calm-small"
headers = {"Authorization": f"Bearer {st.secrets['HF_API_TOKEN']}"}


from transformers import AutoTokenizer, AutoModelForCausalLM

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("無料LLMデモアプリ")

prompt = st.text_area("入力プロンプトを記入してください:", "Streamlitとは何ですか？")

if st.button("回答生成"):
    with st.spinner("生成中です..."):
        output = query({"inputs": prompt})
        result = output[0]['generated_text'] if output else "エラーが発生しました。"
        st.markdown(result)
