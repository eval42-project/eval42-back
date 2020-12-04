from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def dev():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


def prod():
    uvicorn.run("app.main:app", host="0.0.0.0", port=80)
