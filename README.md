This project is a practical exploration of modern agentic AI development, built to test the integration of several key technologies. 

Using a simple TODO list as a sandbox, it demonstrates how to build an application where a user can interact with both a standard web UI and a conversational LangChain agent. 

The primary goal was to experiment with core agentic patterns, such as equipping an LLM with tools to modify a database, ensuring the UI (built with FastAPI and HTMX) stays synchronized with the agent's actions, and implementing ChatGPT-style response streaming for a fluid user experience.



![agentic-todo](https://github.com/user-attachments/assets/ab4f06d2-a9d6-47db-8cd8-c339c73fd4d2)


**Setup:**

**Get your own OpenAI API key:**

https://platform.openai.com/docs/overview

then:

Create a `.env` file in project root directory.  
Add the following line to your `.env` file, replacing `sk-...` with your actual API key:

OPENAI_API_KEY=sk-...

(See `.env.example` for reference.)



**Activate venv:**

in project root, run:

windows cmd: `venv\Scripts\activate`



**Install dependencies:**

when in virtual environment, run:

`pip install fastapi uvicorn jinja2 langchain sqlalchemy sqlmodel httpx langchain-community openai python-dotenv`



**Start local server:**

`uvicorn main:app --reload`

