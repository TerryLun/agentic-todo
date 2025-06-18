# models.py
from sqlmodel import SQLModel, Field, Session, create_engine, select

engine = create_engine("sqlite:///todos.db")

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task: str
    done: bool = False

def init_db():
    SQLModel.metadata.create_all(engine)

def get_todos():
    with Session(engine) as session:
        return session.exec(select(Todo)).all()

def add_todo(task: str):
    with Session(engine) as session:
        session.add(Todo(task=task))
        session.commit()

def update_todo(todo_id: int, new_task: str):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if todo:
            todo.task = new_task
            session.add(todo)  # Optional but good practice
            session.commit()

def delete_todo(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if todo:
            session.delete(todo)
            session.commit()