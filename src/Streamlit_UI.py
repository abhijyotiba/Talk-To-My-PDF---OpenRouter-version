import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #FFFFFF;
        }
        .stChatInput input {
            background-color: #1E1E1E !important;
            color: #FFFFFF !important;
            border: 1px solid #3A3A3A !important;
        }
        .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
            background-color: #1E1E1E !important;
            border: 1px solid #3A3A3A !important;
            color: #E0E0E0 !important;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
            background-color: #2A2A2A !important;
            border: 1px solid #404040 !important;
            color: #F0F0F0 !important;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .stChatMessage .avatar {
            background-color:rgb(214, 230, 225) !important;
            color: #000000 !important;
        }
        .stFileUploader {
            background-color: #1E1E1E;
            border: 1px solid #3A3A3A;
            border-radius: 5px;
            padding: 15px;
        }
        h1, h2, h3 {
            color:rgb(220, 230, 227) !important;
        }
        </style>
        """, unsafe_allow_html=True)
