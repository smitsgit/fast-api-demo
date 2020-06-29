from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    webxnet = "webxnet"


@app.get("/items/{item_name}")
def get_items(item_name: ModelName):
    if item_name == ModelName.alexnet:
        print("Hello world")
    else:
        print("Bye Bye")
    return {'item_name': item_name}
