from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import os

ip_address = os.environ.get("IP_ADDRESS")
port_soma = os.environ.get("PORT_SOMA")

app = FastAPI()

class Multiplicacao(BaseModel):
	num1: int
	num2: int

@app.post("/")
async def calcular(req: Multiplicacao):
    cont = 0
    acc = 0
    while cont < req.num1:
        data = json.dumps({'num1':acc, 'num2':req.num2})
        response = requests.post(ip_address + ":" + port_soma, headers={'Content-type':'application/json'},data=data)
        result = json.loads(response.content.decode("utf-8"))
        acc = result['resultado']
        cont += 1
    return {"resultado": acc}
