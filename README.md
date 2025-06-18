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
