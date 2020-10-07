from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Soma(BaseModel):
	num1: int
	num2: int

@app.post("/")
async def calcular(req: Soma):
    print("REQ NA SOMA:",req)
    return {"resultado": req.num1 + req.num2}
