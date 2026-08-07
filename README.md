# Local AI Agent

A local AI assistant built with **FastAPI**, **Streamlit**, **Ollama**, and **Gemma 4**. The application runs entirely on a local machine, providing a simple web interface for interacting with a large language model without relying on external APIs or cloud services.

This project was created as a hands-on learning exercise to better understand how modern AI applications are structured, from the backend API to the user interface and model integration.

## Features

- Run Gemma 4 locally using Ollama
- FastAPI backend for handling requests
- Streamlit web interface
- Local inference with no external AI APIs
- Modular project structure for future expansion
- Optimized for Apple Silicon

## Tech Stack

- Python
- FastAPI
- Streamlit
- Ollama
- Gemma 4
- Uvicorn

## Project Structure

```text
local-ai-agent/
├── backend/
│   ├── main.py
│   └── ...
├── data/
├── docs/
├── frontend/
│   ├── app.py
│   └── ...
├── tests/
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11+
- Ollama installed
- Gemma 4 downloaded through Ollama

### Installation

Clone the repository:

```bash
git clone https://github.com/EdEsquivel/ai-agent.git
cd ai-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

In another terminal, launch the Streamlit application:

```bash
streamlit run frontend/app.py
```

Make sure Ollama is running before starting the application.

## Why This Project?

The goal of this project is to explore how to build AI applications that run completely on local hardware. It focuses on learning how different components work together, including:

- REST APIs with FastAPI
- Local LLM inference using Ollama
- Frontend development with Streamlit
- Communication between frontend, backend, and the language model

## Future Improvements

Some features planned for future versions include:

- Conversation history
- Retrieval-Augmented Generation (RAG)
- PDF and document analysis
- Voice input and speech output
- Tool calling
- Docker support
- Authentication
- Multi-model support

## License

This project is available under the MIT License.