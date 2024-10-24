import openai
from openai import OpenAI
import streamlit as st
import os
from  dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)

def summarize_text(text):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Summarize this {text}",
        }
    ],
    model="gpt-3.5-turbo",
)
    summary = response.choices[0].message.content
    return summary
st.title("Text Summarizer")

user_input = st.text_area("Enter text you want to summarize:")

if st.button("Summarize"):
    if user_input:
        with st.spinner("Summarizing..."):
            summary = summarize_text(user_input)
            st.subheader("Summary:")
            st.write(summary)

    else:
        st.warning("Please enter text to summarize.")