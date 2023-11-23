# from typing import Union

# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# # https://localhost:8000/
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}



# # https://localhost:8000/item/1
# # https://localhost:8000/item/2
# # https://localhost:8000/item/3
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None): # null값을 허용
#     print(item_id+20)
#     print(q)
#     return {"아이템 아이디 ": item_id, "결과 ": q}



# @app.post("/test")
# def test():
#     pass

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=9000, reload=True)
    

from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
import uvicorn  # 이 부분이 추가되어야 합니다.

app = FastAPI()
class Item(BaseModel): #nameing convention class는 첫글자를 두글자로... 카멜표기?
    name: str # 상속? 
    price: float
    is_offer: Union[bool, None] = None #값이 들어갈 수 도 아닐 수도 


# https://localhost:8000/
@app.get("/itens/")
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


@app.post("/test")
def test():
    pass

   
@app.put("/items/{item_id}") #decoration 
def update_item(item_id: int, item: Item):
    #비즈니스 로직 구현
     return {"item_name":item.name, "item_id": item_id}
 
 
@app.delete("/test_delet")
def test():
    pass
 
if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
    
    