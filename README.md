# Firm Intelligence Bot

Firm Intelligence Bot is an AI-powered conversational chatbot that helps users interact with and extract insights from documents related to firm management. It leverages cutting-edge AI models like mistral for conversational capabilities and provides an intuitive interface for users to ask questions and resolve queries about their documents.

## Features

- **Conversational AI**: Engages in a natural dialogue with users to answer queries.
- **Document Retrieval**: Processes and retrieves insights from `.pdf`, `.docx`, and `.txt` files.
- **Custom Model Selection**: Choose between supported AI models for personalized performance.
- **Persistent Memory**: Maintains conversation context for a seamless chat experience.
- **Vector Store Integration**: Efficiently retrieves relevant document chunks using Chroma.

## Technology Stack

- **Frontend**: Streamlit for user interface and `streamlit_chat` for chat rendering.
- **Backend**: LangChain for conversational retrieval chains, HuggingFace for embeddings, and Chroma for vector storage.
- **AI Model**: Groq's `ChatGroq` for conversational capabilities.
- **Utilities**: `dotenv` for environment variable management, document loaders for various file types.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/firm-intelligence-bot.git
   cd firm-intelligence-bot

2. **Set Up a Virtual Environment:**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate```

3. **Install Dependencies:**
 
   ``` pip install -r requirements.txt```


