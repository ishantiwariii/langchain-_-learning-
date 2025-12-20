from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature= 0.3
    )

st.header('Reasearch Tool')

prompt = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = llm.invoke(prompt)
    st.write(result.content)