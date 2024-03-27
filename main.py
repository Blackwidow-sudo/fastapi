from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from os import getenv

app = FastAPI()

API_KEY = getenv('API_KEY', 'secret-key')
API_KEY_HEADER = getenv('API_KEY_HEADER', 'X-API-Key')

@app.middleware('http')
async def validate_api_key(request: Request, call_next):
    api_key = request.headers.get(API_KEY_HEADER)

    if api_key != API_KEY:
        return JSONResponse(
            status_code=401,
            content="Could not validate API key"
        )
    
    response = await call_next(request)

    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/secure")
def secure_endpoint():
    return {"message": "You have access to this secure endpoint!"}