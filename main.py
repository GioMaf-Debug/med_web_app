from fastapi import FastAPI, Query, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

# ✅ Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# ✅ Path Parameter Example
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# ✅ Query Parameters Example
@app.get("/search/")
def search(
    query: str = Query(..., description="Search query"), 
    page: int = Query(1, description="Page number"), 
    size: int = Query(10, description="Number of results per page")
):
    return {"query": query, "page": page, "size": size}

# ✅ Request Body (POST)
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# ✅ Background Tasks Example
def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")

@app.post("/log/")
def log_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Log scheduled"}

# ✅ Authentication Example (OAuth2 Placeholder)
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
