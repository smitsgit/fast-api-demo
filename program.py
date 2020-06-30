from fastapi import FastAPI
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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {'item_id': item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    data = {'name': "Smital", 'price': "test", 'is_offer': True}
    dm = Item(name=10, price='hello', is_offer=10)
    return {"item_price": item.price}
