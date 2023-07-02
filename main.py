from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
async def root():
  return {"greeting":"Hello world"}

@app.get("/api/v1/users")
async def get_users():
  return db

@app.post("/api/v1/users")
async def create_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
  raise HTTPException(
    status_code=404, detail=f"Delete user failed, id {id} not found."
  )
@app.put("/api/v1/users/{id}")
async def update_user(user_update: User, id: UUID):
  for user in db:
    if user.id == id:
      if user_update.first_name is not None:
        user.first_name = user_update.first_name
        if user_update.last_name is not None:
          user.last_name = user_update.last_name
          if user_update.roles is not None:
            user.roles = user_update.roles
            return user.id
            raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")

db: List[User] = [
         User(
              id=uuid4(),
               first_name="Vinay",
                last_name="Bhandari",
                 gender=Gender.male,
                  roles=[Role.user],
                   ),
          User(
               id=uuid4(),
                first_name="Shelly",
                 last_name="Bhandari",
                  gender=Gender.female,
                   roles=[Role.user],
                    ),
           User(
                id=uuid4(),
                 first_name="Ritu",
                  last_name="Bhandari",
                   gender=Gender.male,
                    roles=[Role.user],
                     ),
            User(
                 id=uuid4(),
                  first_name="AKC",
                   last_name="AKC",
                    gender=Gender.male,
                     roles=[Role.admin, Role.user],
                      ),
            ]
