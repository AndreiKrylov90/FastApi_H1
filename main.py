from fastapi import FastAPI
from pydantic import BaseModel
from random import choice

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []

for i in range(1, 11):
    new_user = User(
    id=i,
    name=f"name{i}",
    email=f"email{i}",
    password=f"password{i}"
    )
    users.append(new_user)


@app.get("/")
async def get_users():
    return users


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i, m in enumerate(users):
        if m.id == user_id:
            users[i] = user
            return user
    return {"message": "User was not found"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User was removed"}
    return {"message": "User was not found"}