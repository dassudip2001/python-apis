from fastapi import FastAPI
from typing import Union
from model import User
app = FastAPI()

db: List[User] = [
    User(username="user1", email="user",
]

@app.get("/")
def read_root():
    return {"Hello": "World"}