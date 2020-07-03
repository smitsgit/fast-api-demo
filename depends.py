"""
This is really useful when you need to have
- shared logic
- shared database connections
- Enforce security, authentication and roles enforcement
- And many other things

The simplicity of the dependency makes Fastapi compatible with
- All the relational databases
- NoSql databases
- external apis
- authentication and authorization systems
- api usage monitoring
- response data injection systems
"""


from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()


def common_params(q: Optional[str] = None, skip: int = 0, limit: int = 5):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items")
def get_items(common_params: dict = Depends(common_params)):
    return common_params


@app.get("/users")
def list_users(common_params: dict = Depends(common_params)):
    return common_params
