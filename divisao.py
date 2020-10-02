from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

class Divisao(BaseModel):
	num1: int
	num2: int

@app.post("/divisao")
async def calcular(req: Divisao):
    cont = 0
    while req.num1 >= req.num2:
        response = requests.post("http://subtracao:8200/subtracao", headers={'Content-type':'application/json'},data='{"num1":' + str(req.num1) + ',"num2":' + str(req.num2) + '}')
        result = json.loads(response.content.decode("utf-8"))
        print(result)
        req.num1 = result['resultado']
        cont += 1
    return {"resultado": cont}
