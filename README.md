This project is a practical exploration of modern agentic AI development, built to test the integration of several key technologies. Using a simple TODO list as a sandbox, it demonstrates how to build an application where a user can interact with both a standard web UI and a conversational LangChain agent. The primary goal was to experiment with core agentic patterns, such as equipping an LLM with tools to modify a database, ensuring the UI (built with FastAPI and HTMX) stays synchronized with the agent's actions, and implementing ChatGPT-style response streaming for a fluid user experience.

![20250617-1](https://github.com/user-attachments/assets/1f16ff9e-19fb-4462-9123-70eecc89b2b0)
![20250620-1](https://github.com/user-attachments/assets/a970417f-4dbb-4366-bc56-28e11b5fa84c)


**Activate venv:**

in project root, run:

windows cmd: `venv\Scripts\activate`



**Install dependencies:**

when in virtual environment, run:

`pip install fastapi uvicorn jinja2 langchain sqlalchemy sqlmodel httpx langchain-community openai`



**Set openai api key:**

windows cmd: `set OPENAI_API_KEY=sk-yourkeyhere`



**Start local server:**

uvicorn main:app --reload

