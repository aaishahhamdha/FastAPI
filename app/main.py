# main.py
from fastapi import FastAPI, Body
from typing import Optional
import uvicorn

app = FastAPI()

# 1. GET - Root endpoint
@app.get("/")
def root():
    return {"message": "Hello, This is the sample service I just created!"}

# 2. GET - Greet with path parameter and optional query
@app.get("/greet/{name}")
def greet_user(name: str, age: Optional[int] = None):
    if age:
        return {"message": f"Hello {name}, you are {age} years old!"}
    return {"message": f"Hello {name}!"}

# 3. POST - Echo back data
@app.post("/echo/")
def echo_data(data: dict = Body(...)):
    return {"you_sent": data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

