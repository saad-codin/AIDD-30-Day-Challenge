# PDF Summarizer with AI Agent

This Streamlit application allows you to upload one or more PDF files and generates concise, meaningful summaries using the OpenAI API.

## Features

- **Upload Multiple PDFs:** Easily upload multiple PDF documents for summarization.
- **AI-Powered Summarization:** Leverages OpenAI's language models (`gpt-3.5-turbo`) to generate high-quality summaries.
- **Large PDF Handling:** Automatically splits large PDFs into chunks, summarizes each chunk, and then synthesizes these into a comprehensive final summary (map-reduce approach).
- **Clean UI:** A user-friendly interface built with Streamlit, featuring card-style display for summaries.
- **Download Summaries:** Option to download each generated summary as a text file.

## Setup and Installation

Follow these steps to set up and run the application locally:

### 1. Clone the repository (if not already done)

```bash
git clone <your-repository-url>
cd pdfsummarizer
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 4. Install Dependencies

Install the required Python packages using `pip` from your `pyproject.toml` file.

```bash
pip install -e .
```
(Note: `-e .` installs the package in editable mode, which is suitable for development and picks up dependencies from `pyproject.toml`.)

### 5. Set up your OpenAI API Key

The application requires an OpenAI API key to generate summaries. Streamlit securely handles API keys using `secrets.toml`.

1.  Create a folder named `.streamlit` in your project's root directory (if it doesn't already exist).
2.  Inside the `.streamlit` folder, create a file named `secrets.toml`.
3.  Add your OpenAI API key to `secrets.toml` in the following format:

    ```toml
    openai_api_key = "your_openai_api_key_here"
    ```
    Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

    **Example directory structure:**
    ```
    pdfsummarizer/
    ├── .streamlit/
    │   └── secrets.toml
    ├── main.py
    ├── pyproject.toml
    └── ...
    ```

### 6. Run the Streamlit Application

With your virtual environment activated and API key configured, run the application:

```bash
streamlit run main.py
```

This command will open the application in your web browser. You can then upload your PDF files and get summaries.

---

Feel free to contribute or suggest improvements!
