# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI, Path
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette import status
import uvicorn

# On instancie le webservice
app = FastAPI()

class Todo(BaseModel):
    id: int
    content: str

todos = {
    1: Todo(id=1, content="Step 1 : "),
    2: Todo(id=2, content="Step 2 : "),
    3: Todo(id=3, content="Step 3 : "),
    4: Todo(id=4, content="Step 4 : "),
}

# Définition du endpoint get /todo
@app.get("/todo")
async def get_all_todo():
    return todos.values()

# Définition du endpoint get /todo/{id_todo}
@app.get("/todo/{id_todo}")
async def get_todo_by_id(id_todo: int = Path(..., description="The `id` of the todo you want to get")):
    todo = todos.get(id_todo)
    if todo:
        return todo
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Todo not found"})

# Définition du endpoint post /todo
@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def post_todo(todo: Todo):
    if todo.id not in todos:
        todos[todo.id] = todo
        return todo
    else:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"message": "Todo with this id already exists"})

#Définiton pour ajouter un nouvel utilisateur en utilisant POST
@app.post("/nx_util", status_code=status.HTTP_201_CREATED)
async def nx_util(id,mdp):
    creer_util(id,mdp)#il faut utiliser la mathode que Bastien aura créé pour créer un utilisateur

# Lancement de l'application sur le port 8151
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8151)


