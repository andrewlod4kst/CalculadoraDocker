from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Subtracao(BaseModel):
	num1: int
	num2: int

@app.post("/")
async def calcular(req: Subtracao):
    return {"resultado": req.num1 - req.num2}
