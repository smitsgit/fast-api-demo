from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/items")
def get_items(q: str, skip: int = 0, limit: int = 10, order: Optional[str] = None):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip: skip + limit]
