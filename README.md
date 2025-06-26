# 📄 Talk-To-My-PDF - AI Document Assistant

An intelligent PDF analysis tool powered by LangChain and Streamlit that lets you converse with your documents. Upload PDFs and get instant answers to your questions through an AI-powered chat interface.

---

## ✨ Features

- 🗂️ PDF document ingestion and processing
- 🔍 Semantic search and document retrieval
- 💬 Natural language Q&A with uploaded documents
- 🎨 Custom dark-mode Streamlit UI
- 🧠 Powered by Mistral AI via OpenRouter (or local Ollama models)
- 📝 Context-aware answers with document citations

---

### Workflow Diagram
<p align="center">
  <img src="https://i.postimg.cc/5tPVqXSy/Mermaid-Chart-Create-complex-visual-diagrams-with-text-A-smarter-way-of-creating-diagrams-2025.png" width="500" height="600"/>
</p>




## 🛠️ Tech Stack

- **LangChain** - Document processing and AI orchestration
- **Streamlit** - Web interface
- **OpenRouter/Mistral** - AI model backend (or Ollama for local)
- **HuggingFace Embeddings** - Document vectorization
- **PDFPlumber** - PDF text extraction
- **Python** - Backend logic

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/abhtjyotibs/Talk-To-My-PDF---Ollama-version.git
cd Talk-To-My-PDF---Ollama-version
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux/macOS
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a `.env` file with your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Upload a PDF document through the interface
2. Wait for document processing to complete
3. Ask questions about the document content in natural language
4. Receive accurate, context-aware answers

<p align="center">
  <img src="https://i.postimg.cc/tTYc9LzB/Screenshot-2025-06-24-213854.png" width="700"/>
</p>

---

<p align="center">
  <img src="https://i.postimg.cc/Znm6wN06/Screenshot-2025-06-24-213912.png" width="700"/>
</p>

---

## 🔄 Alternative: Local Ollama Setup

To run with local models instead of OpenRouter:

1. Install [Ollama](https://ollama.com/)
2. Pull a compatible model:
```bash
ollama pull mistral
```
3. Modify `helper.py` to use Ollama instead of OpenRouter

---

## 🏗️ Project Structure

```
├── app.py               # Main Streamlit application
├── helper.py            # Core document processing logic
├── Streamlit_UI.py      # Custom UI components
├── requirements.txt     # Python dependencies
└── document_store/      # Uploaded PDF storage
```

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---


