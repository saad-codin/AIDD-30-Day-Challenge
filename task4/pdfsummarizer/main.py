import streamlit as st
import PyPDF2
from openai import OpenAI
import os
import io

# --- Helper Functions ---

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.
    Args:
        pdf_file: UploadedFile object from Streamlit.
    Returns:
        A string containing all extracted text, or None if an error occurs.
    """
    try:
        # Create a file-like object for PyPDF2
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        st.error(f"Error reading PDF '{pdf_file.name}': {e}")
        return None

def get_summary_from_llm(text, openai_client, prompt_prefix="Please summarize the following text:"):
    """
    Generates a summary for a given text using the OpenAI LLM.
    Args:
        text (str): The text to be summarized.
        openai_client: An initialized OpenAI client instance.
        prompt_prefix (str): Prefix for the summarization prompt.
    Returns:
        A string containing the summary, or None if an error occurs.
    """
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo", # You can choose a different model if preferred
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text concisely."}, 
                {"role": "user", "content": f"{prompt_prefix}\n\n{text}"}
            ],
            temperature=0.5,
            max_tokens=500 # Limit summary length
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

def summarize_large_text(large_text, openai_client, max_chunk_size=3000, final_summary_prompt="Please synthesize the following summaries into one comprehensive summary:"):
    """
    Summarizes very large texts by breaking them into chunks, summarizing each chunk,
    and then synthesizing those summaries into a final comprehensive summary (map-reduce).
    Args:
        large_text (str): The extensive text to summarize.
        openai_client: An initialized OpenAI client instance.
        max_chunk_size (int): Maximum character length for each text chunk.
        final_summary_prompt (str): Prompt for the final summarization of combined chunk summaries.
    Returns:
        A string containing the final comprehensive summary, or None if an error occurs.
    """
    if not large_text:
        return None

    # Split the text into chunks
    # Simple chunking by character count; more sophisticated methods could be used
    # based on token count or sentence boundaries.
    chunks = [large_text[i:i + max_chunk_size] for i in range(0, len(large_text), max_chunk_size)]

    if len(chunks) == 1:
        # If only one chunk, summarize directly
        return get_summary_from_llm(chunks[0], openai_client)

    # Summarize each chunk (Map step)
    chunk_summaries = []
    st.info(f"Splitting PDF into {len(chunks)} parts for summarization...")
    for i, chunk in enumerate(chunks):
        with st.spinner(f"Summarizing part {i+1}/{len(chunks)}..."):
            summary = get_summary_from_llm(chunk, openai_client)
            if summary:
                chunk_summaries.append(summary)
            else:
                st.warning(f"Could not summarize part {i+1}. Skipping.")
    
    if not chunk_summaries:
        return "Could not generate any summaries for the PDF parts."

    # Combine chunk summaries and get a final summary (Reduce step)
    combined_chunk_summaries = "\n\n---\n\n".join(chunk_summaries)
    st.info("Synthesizing final summary from chunk summaries...")
    final_summary = get_summary_from_llm(combined_chunk_summaries, openai_client, prompt_prefix=final_summary_prompt)
    
    return final_summary

# --- Streamlit UI Configuration ---

st.set_page_config(
    page_title="PDF Summarizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📄 AI-Powered PDF Summarizer")
st.markdown(
    """
    Upload one or more PDF files, and I'll generate concise, meaningful summaries for you.
    This app uses **PyPDF2** for text extraction and the **OpenAI API** for summarization.
    """
)

# --- OpenAI API Key Handling ---
# Use Streamlit secrets for API key management
# Users should set this in their .streamlit/secrets.toml file:
# openai_api_key = "YOUR_OPENAI_API_KEY"
try:
    openai_api_key = st.secrets["openai_api_key"]
    openai_client = OpenAI(api_key=openai_api_key)
except KeyError:
    st.error(
        "OpenAI API key not found in Streamlit secrets. "
        "Please add it to your `.streamlit/secrets.toml` file like: `openai_api_key = 'YOUR_KEY'`"
    )
    st.stop() # Stop the app if API key is not available
except Exception as e:
    st.error(f"Error initializing OpenAI client: {e}")
    st.stop()

# --- File Uploader ---
st.sidebar.header("Upload PDFs")
uploaded_files = st.sidebar.file_uploader(
    "Choose one or more PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    st.header("Summaries")
    for i, uploaded_file in enumerate(uploaded_files):
        st.subheader(f"Summary for: `{uploaded_file.name}`", divider="blue")

        # --- Processing and Summary Generation ---
        with st.spinner(f"Extracting text from '{uploaded_file.name}' and generating summary..."):
            extracted_text = extract_text_from_pdf(uploaded_file)

            if extracted_text:
                summary = summarize_large_text(extracted_text, openai_client)

                if summary:
                    # --- Display Summary Card ---
                    st.markdown(
                        f"""
                        <div style=\
                            border: 1px solid #e6e6e6; 
                            border-left: 5px solid #4CAF50; 
                            border-radius: 8px; 
                            padding: 20px; 
                            margin-bottom: 20px; 
                            background-color: #f9f9f9; 
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        \">
                            <p style=\"font-size: 16px; color: #333333; line-height: 1.6;\">{summary}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --- Download Button ---
                    st.download_button(
                        label="Download Summary",
                        data=summary.encode("utf-8"),
                        file_name=f"summary_{uploaded_file.name.replace('.pdf', '')}.txt",
                        mime="text/plain",
                        key=f"download_button_{i}" # Unique key for multiple buttons
                    )
                else:
                    st.warning(f"Could not generate a summary for '{uploaded_file.name}'.")
            else:
                st.error(f"Failed to extract text from '{uploaded_file.name}'.")
        st.markdown("---") # Separator between summaries

else:
    st.info("Upload your PDF files using the sidebar to get started!")

# --- Footer ---
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f2f6;
            color: #333;
            text-align: center;
            padding: 10px;
            font-size: 0.9em;
            border-top: 1px solid #e6e6e6;
        }
    </style>
    <div class="footer">
        <p>Built with ❤️ by Gemini</p>
    </div>
    """,
    unsafe_allow_html=True
)
