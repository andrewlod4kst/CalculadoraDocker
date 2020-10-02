from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

class Multiplicacao(BaseModel):
	num1: int
	num2: int

@app.post("/multiplicacao")
async def calcular(req: Multiplicacao):
    cont = 0
    acc = 0
    while cont < req.num1:
        response = requests.post("http://soma:8100/soma", headers={'Content-type':'application/json'},data='{"num1":' + str(acc) + ',"num2":' + str(req.num2) + '}')
        result = json.loads(response.content.decode("utf-8"))
        acc = result['resultado']
        cont += 1
    return {"resultado": acc}
