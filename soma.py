from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Soma(BaseModel):
	num1: int
	num2: int

@app.post("/soma")
async def calcular(req: Soma):
    return {"resultado": req.num1 + req.num2}