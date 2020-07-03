from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse


class Err(BaseModel):
    err: str


app = FastAPI()

items = {
    10: "Hello",
    20: "Gello",
}


class UnicornException(Exception):
    def __init__(self, name):
        self.name = name


@app.exception_handler(UnicornException)
def handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=404, content={
        "error": "What the ckuk"
    })


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise UnicornException("Grrrr")
    # if item_id not in items:
    #     raise HTTPException(status_code=404, headers={
    #         'X-code': 'whats up'
    #     }, detail=Err(err="not finding").dict())
    return {'item': items[item_id]}
