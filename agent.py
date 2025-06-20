# agent.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool
from models import add_todo, delete_todo, get_todos, update_todo

@tool
def add_item(task: str) -> str:
    """Add a new todo item to the list."""
    add_todo(task)
    return f"Added: {task}"

@tool
def delete_item(task: str) -> str:
    """Delete a todo item by exact match."""
    for t in get_todos():
        if t.task.lower() == task.lower() and t.id is not None:
            delete_todo(t.id)
            return f"Deleted: {task}"
    return f"Task not found: {task}"

@tool
def update_item(old: str, new: str) -> str:
    """Update an existing todo item from old text to new text."""
    for t in get_todos():
        if t.task.lower() == old.lower() and t.id is not None:
            update_todo(t.id, new)
            return f"Updated: {old} → {new}"
    return f"Task not found: {old}"

tools = [add_item, delete_item, update_item]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful todo assistant. Please read carefully what user's intention and use tools when appropriate."),
    MessagesPlaceholder("chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

agent_runnable: Runnable = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor: AgentExecutor = AgentExecutor(agent=agent_runnable, tools=tools, verbose=True)

def handle_chat(user_input: str) -> str:
    result = agent_executor.invoke({
        "input": user_input,
        "chat_history": [],
    })
    return result["output"]