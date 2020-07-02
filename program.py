from typing import Optional

from fastapi import FastAPI, Cookie, Header, Form
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

    class Config:
        schema_extra = {
            "example": {
                "name": "foo",
                "price": 10.5,
                "is_offer": True
            }
        }


@app.get("/")
def hello_world():
    return {'name': 'Smital', 'surname': 'Desai'}


@app.get("/items")
def read_cookie(ads_id: Optional[str] = Cookie(None),
                user_agent: Optional[str] = Header(None)):
    """
    HTTP clients send cookies to the server as regular HTTP headers.
    That means, HTTPie does not offer any special syntax for specifying cookies

    http http://127.0.0.1:8000/items Cookie:ads_id='121242'
    """
    return {"cookie": ads_id, "User-Agent": user_agent}


@app.put("/items", response_model=Item, response_model_exclude={'is_offer'})
def create_item():
    # return Item(name="Smota", price=52.5, is_offer=True)
    return {'name': 'GSmota', 'price': 52.5}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {'item_id': item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    data = {'name': "Smital", 'price': "test", 'is_offer': True}
    dm = Item(name=10, price='hello', is_offer=10)
    return {"item_price": item.price}


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
