from google import genai  
import os
import streamlit as st
from dotenv import load_dotenv


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI Setup
st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.markdown("""
    <style>
    .stTextInput input {
        font-size: 16px;
        padding: 10px;
    }
    .stButton>button {
        font-size: 16px;
        padding: 8px 20px;
        background-color: #4CAF50;
        color: white;
    }
    .stMarkdown h3 {
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Gemini Chat Interface")
st.markdown("Hi, Hello! I'm Gemini...")


user_input = st.text_input("User:")


if user_input:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        # Display response in Streamlit
        st.markdown("### Gemini:")
        st.success(str(response.text))
    except Exception as e:
        st.error(f"Error: {e}")
