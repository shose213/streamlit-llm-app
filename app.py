import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# ---- 設定 ----
st.set_page_config(page_title="専門家チャット", page_icon="🧠")

# ---- アプリの説明 ----
st.title("🧠 専門家と話そう！")
st.markdown("""
このアプリでは、あなたの入力内容に対して2人の専門家が回答してくれます。  
ラジオボタンで専門家を選び、入力フォームに質問や相談内容を入力して送信してください。
""")

# ---- 専門家の選択 ----
expert = st.radio(
    "以下の専門家から選んでください：",
    ["健康アドバイザー", "ビジネスコンサルタント"]
)

# ---- 入力フォーム ----
user_input = st.text_input("質問や相談内容を入力してください：")

# ---- 専門家ごとのシステムプロンプト ----
def get_system_prompt(expert_choice):
    if expert_choice == "健康アドバイザー":
        return "あなたは経験豊富な健康アドバイザーです。専門的でありながら、やさしく分かりやすく回答してください。"
    elif expert_choice == "ビジネスコンサルタント":
        return "あなたは一流のビジネスコンサルタントです。経営やマーケティングについて論理的にアドバイスを提供してください。"
    else:
        return "あなたは博識なアシスタントです。"

# ---- 回答生成関数 ----
def generate_response(input_text, expert_choice):
    system_prompt = get_system_prompt(expert_choice)

    chat = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_text)
    ]

    response = chat(messages)
    return response.content

# ---- 回答表示 ----
if user_input:
    with st.spinner("回答を生成中..."):
        output = generate_response(user_input, expert)
        st.markdown("### 回答：")
        st.write(output)
