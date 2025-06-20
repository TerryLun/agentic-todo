# venv\Scripts\activate  (cmd)
# uvicorn main:app --reload

# main.py
from fastapi import FastAPI, Request, Form, Path
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import init_db, get_todos, add_todo, update_todo, delete_todo
from agent import handle_chat

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

@app.post("/edit/{todo_id}", response_class=HTMLResponse)
async def edit(request: Request, todo_id: int, task: str = Form(...)):
    if task.strip():
        update_todo(todo_id, task.strip())
    todos = get_todos()
    html = templates.get_template("partials/todo_items.html").render(todos=todos)
    return HTMLResponse(content=html)

@app.post("/delete/{todo_id}", response_class=HTMLResponse)
async def delete(request: Request, todo_id: int):
    delete_todo(todo_id)
    todos = get_todos()
    html = templates.get_template("partials/todo_items.html").render(todos=todos)
    return HTMLResponse(content=html)

@app.post("/chat")
async def chat(request: Request, message: str = Form(...)):
    return StreamingResponse(handle_chat(message), media_type="text/plain")

@app.get("/partial/todos", response_class=HTMLResponse)
async def partial_todo(request: Request):
    todos = get_todos()
    html = templates.get_template("partials/todo_items.html").render(todos=todos)
    return HTMLResponse(content=html)