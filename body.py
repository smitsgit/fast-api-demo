from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.put("/items")
def update_items(item: Item):  # = Body(..., embed=True)):
    return {"item_name": item.name, "item_price": item.price}
