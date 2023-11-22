from typing import Union

from fastapi import FastAPI

app = FastAPI()

# https://localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

# https://localhost:8000/item/1
# https://localhost:8000/item/2
# https://localhost:8000/item/3
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # null값을 허용
    print(item_id+20)
    print(q)
    return {"아이템 아이디 ": item_id, "결과 ": q}
