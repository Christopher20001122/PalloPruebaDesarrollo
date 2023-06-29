from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: int):
    return {"message": name}

@app.post("/hello")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}

