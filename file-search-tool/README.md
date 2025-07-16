# 📂 AI File Search Assistant — Powered by OpenAI + Chainlit

This project is a conversational assistant that uses OpenAI's **Function Calling Agents** and **FileSearchTool** to answer user questions using uploaded documents (via Vector Stores), wrapped inside a **Chainlit UI**.

> 🔍 Ask your documents anything — the agent will respond using live file-based search.

---

## ✨ Features

- ✅ Built with [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- ✅ Supports [FileSearchTool](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.FileSearchTool)
- ✅ Chat UI using [Chainlit](https://docs.chainlit.io/)
- ✅ CLI mode for quick testing
- ✅ .env-based secure API configuration
- ✅ Upload your own `.txt` or `.pdf` knowledge base

---

## 🚀 Demo Preview

> 👤: Where is DUET located?

🤖: Dawood University of Engineering and Technology (DUET) is located in Karachi, Pakistan.


---

## 📦 Installation

```bash
git clone https://github.com/raza-ahmed-khan360/file-search-tool.git
cd file-search-tool

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# Install dependencies
uv pip install -r pyproject.toml
```
## 🔐 Setup
Create a .env file in the root directory:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
VECTOR_STORE_ID=vs_abc123xyz456
#Place your data in a knowledge.txt file (or another .txt file).
```

## 📁 Upload File to Vector Store
Run this script to upload your file and get the vector_store_id:
```python upload_vector_store.py```
Replace the vector store ID in your agent code:
```bash

file_search_tool = FileSearchTool(vector_store_ids=["vs_abc123..."])
💬 Run with Chainlit

chainlit run main.py
Then open your browser at: http://localhost:8000
```

## 🧪 CLI Mode (Optional)
To test without UI:
```bash
#python main.py
🧠 Sample Questions
What gases make up the Earth's atmosphere?

Where is Dawood University of Engineering and Technology?

What is GPT-4?

At what temperature does water freeze?

```
## 📂 Project Structure
```bash
.
├── main.py                   # Chainlit + Agent code
├── upload_vector_store.py    # File uploader to vector store
├── knowledge.txt             # Your knowledge base
├── .env                      # OpenAI API Key
├── requirements.txt
└── README.md
```

## 🤝 Acknowledgements

1. [OpenAI Agents SDK](https://openai.github.io/openai-agents-python)
2. [Chainlit](https://docs.chainlit.io/)
