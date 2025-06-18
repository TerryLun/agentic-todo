# venv\Scripts\activate  (cmd)
# uvicorn main:app --reload

# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import init_db, get_todos, add_todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    todos = get_todos()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add", response_class=HTMLResponse)
async def add(request: Request, task: str = Form(...)):
    add_todo(task)
    todos = get_todos()
    html = templates.get_template("partials/todo_items.html").render(todos=todos)
    return HTMLResponse(content=html)

