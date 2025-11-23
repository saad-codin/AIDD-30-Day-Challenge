import streamlit as st
from PyPDF2 import PdfReader
import openai
import os

# --- Configuration ---
# We'll use session state to store various data.
if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = ''
if 'summary' not in st.session_state:
    st.session_state.summary = ''
if 'quiz' not in st.session_state:
    st.session_state.quiz = ''
if 'file_name' not in st.session_state:
    st.session_state.file_name = ''

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# --- UI Setup ---
st.set_page_config(page_title="PDF Summarizer and Quiz Generator", layout="wide")

st.title("📄 PDF Summarizer and Quiz Generator")
st.write("Upload a PDF, get a summary, and generate a quiz!")

# --- API Key Handling ---
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not openai_api_key:
    st.warning("Please set your OpenAI API Key in a .env file (e.g., OPENAI_API_KEY='your_key_here')")
else:
    openai.api_key = openai_api_key


    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.session_state.file_name = uploaded_file.name

        with st.spinner('Extracting text from PDF...'):
            try:
                pdf_reader = PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                st.session_state.pdf_text = text
                st.success("Text extracted successfully!")
            except Exception as e:
                st.error(f"Error extracting text: {e}")
                st.session_state.pdf_text = ''

    if st.session_state.pdf_text:
        st.header(f"Working with: {st.session_state.file_name}")

        # --- Summarization ---
        if st.button("Generate Summary"):
            if st.session_state.pdf_text:
                with st.spinner("Generating summary..."):
                    try:
                        # For very large texts, you might need to chunk it.
                        # This is a simplified example.
                        response = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                                {"role": "user", "content": f"Summarize the following text:\n\n{st.session_state.pdf_text}"}
                            ]
                        )
                        st.session_state.summary = response.choices[0].message.content
                    except Exception as e:
                        st.error(f"Error generating summary: {e}")
                        st.session_state.summary = ''

        if st.session_state.summary:
            st.subheader("Summary")
            st.markdown(f"""
            <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            {st.session_state.summary}
            </div>
            """, unsafe_allow_html=True)

            # --- Quiz Generation ---
            if st.button("Create Quiz"):
                with st.spinner("Generating quiz..."):
                    try:
                        response = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant that creates quizzes from text."},
                                {"role": "user", "content": f"Create a quiz (MCQs and short answer questions) based on the following text:\n\n{st.session_state.pdf_text}"}
                            ]
                        )
                        st.session_state.quiz = response.choices[0].message.content
                    except Exception as e:
                        st.error(f"Error generating quiz: {e}")
                        st.session_state.quiz = ''

        if st.session_state.quiz:
            st.subheader("Quiz")
            st.markdown(f"""
            <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            {st.session_state.quiz}
            </div>
            """, unsafe_allow_html=True)