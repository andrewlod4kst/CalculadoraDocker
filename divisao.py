from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import os

ip_address = os.environ.get("IP_ADDRESS")
port_sub = os.environ.get("PORT_SUB")

app = FastAPI()

class Divisao(BaseModel):
	num1: int
	num2: int

@app.post("/")
async def calcular(req: Divisao):
    cont = 0
    while req.num1 >= req.num2:
        data = json.dumps({'num1':req.num1, 'num2':req.num2})
        response = requests.post(ip_address + ":" + port_sub, headers={'Content-type':'application/json'},data=data)
        result = json.loads(response.content.decode("utf-8"))
        req.num1 = result['resultado']
        cont += 1
    return {"resultado": cont}
