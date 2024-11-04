import sys
sys.path.append("/Users/cpprhtn/Documents/GitHub/AutoML-Study/proj")

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from make_model import *

app = FastAPI()

class set_Data(BaseModel):
    path: str
    max_trials: int
    epochs: int


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/make_model")
def makeModel(data:set_Data):
    result = Training_Model(data.path, data.max_trials, data.epochs)
    response_content = {"status": "success", "result": result}

    return JSONResponse(content=response_content, status_code=200)
