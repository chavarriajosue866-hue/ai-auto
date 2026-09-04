# ai-auto
AI Automation Engine: FastAPI + LangChain + Playwright
🤖 AI Automation Engine
Complete task automation engine powered by Artificial Intelligence. It orchestrates web scraping, form interaction, database management, and repetitive task bypassing using natural language instructions.
✨ Features
AI Brain (LangChain): Interprets natural language prompts and decides which actions to execute via Tool Calling.
Autonomous Hands (Playwright): Asynchronous web navigation, clicks, form filling, and real-time data extraction.
REST API (FastAPI): Asynchronous endpoint to dispatch background tasks without blocking the server.
Persistence (PostgreSQL): Task logging, status tracking, and extracted data storage.
🛠️ Tech Stack
Backend: Python 3.12+, FastAPI, Uvicorn
AI & Agents: LangChain, OpenAI API (GPT-4o)
Web Automation: Playwright (Async API)
Database: PostgreSQL, SQLAlchemy
⚙️ Installation & Setup

Clone the repository and enter the folder:

  1. git clone <your-repo-url>
  2. cd ai-auto
     
Create a virtual environment and install dependencies:
 1.  python -m venv venv
 2.  venv\Scripts\activate  # On Windows
 3.  pip install -r requirements.txt
 4.  playwright install chromium

    Configure environment variables:
Create a .env file in the root directory with your credentials:
1.  DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/ai_automation
2. OPENAI_API_KEY=sk-your_api_key_here

   Setup Database:
Ensure PostgreSQL is running and create the ai_automation database. Tables will be generated automatically upon server startup.
🚀 Usage
Start the server:
1. python -m uvicorn app.main:api_app --reload

    Interact with the API:
Open your browser at http://127.0.0.1:8000/docs to access the interactive Swagger UI.
Run a task:
Send a POST request to /api/tasks/ with a prompt like:
   {
     "prompt": "Go to https://news.ycombinator.com/ and tell me the title of the first news item."
   }
