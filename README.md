# 🤖 AI Automation Engine

Complete task automation engine powered by Artificial Intelligence. It orchestrates web scraping, form interaction, database management, and repetitive task bypassing using natural language instructions.

## ✨ Features

- **AI Brain (LangChain):** Interprets natural language prompts and decides which actions to execute via dynamic *Tool Calling*.
- **Autonomous Hands (Playwright):** Asynchronous web navigation, element clicking, form filling, and real-time DOM data extraction.
- **REST API (FastAPI):** Asynchronous endpoints to dispatch background tasks without blocking the main server thread.
- **Persistence (PostgreSQL):** Robust task logging, status tracking, and extracted data storage via SQLAlchemy.

## 🛠️ Tech Stack

- **Backend:** Python 3.12+, FastAPI, Uvicorn
- **AI & Agents:** LangChain, OpenAI API (GPT-4o)
- **Web Automation:** Playwright (Async API)
- **Database:** PostgreSQL, SQLAlchemy

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chavarriajosue866-hue/ai-auto.git
   cd ai-auto

   python -m venv venv
   # On Windows:
   venv\Scripts\activate  
   # On macOS/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   playwright install chromium

   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/ai_automation
   OPENAI_API_KEY=sk-your_openai_api_key_here

Setup Database:
Ensure PostgreSQL is running and create the ai_automation database. Tables will be generated automatically upon server startup.
🚀 Usage
Start the development server:

   python -m uvicorn app.main:api_app --reload

Interact with the API:
Open your browser at http://127.0.0.1:8000/docs to access the interactive Swagger UI.
Run a task:
Send a POST request to /api/tasks/ with a natural language prompt:

   {
     "prompt": "Go to https://news.ycombinator.com/ and tell me the title of the first news item."
   }

The server will immediately return a task_id, and the AI agent will execute the task in the background, updating the database upon completion.
