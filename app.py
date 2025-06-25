import streamlit as st
from src.Streamlit_UI import apply_custom_css
import os
from src.helper import (
                        save_uploaded_file,
                        load_pdf_documents,
                        chunk_documents,
                        index_documents,
                        find_related_documents,
                        generate_answer
                    )



# UI Configuration


st.title("🤖 Talk To My PDF")
st.markdown("### Your Intelligent Document Assistant")
st.markdown("---")

apply_custom_css()


# File Upload Section logic

uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False

)

if uploaded_pdf:
    saved_path = save_uploaded_file(uploaded_pdf)
    raw_docs = load_pdf_documents(saved_path)
    processed_chunks = chunk_documents(raw_docs)
    index_documents(processed_chunks)
    
    st.success("✅ Document processed successfully! Ask your questions below.")
    
    user_input = st.chat_input("Enter your question about the document...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.spinner("Analyzing document..."):
            relevant_docs = find_related_documents(user_input)
            ai_response = generate_answer(user_input, relevant_docs)
            
        with st.chat_message("assistant", avatar="🤖"):
            st.write(ai_response.content)
