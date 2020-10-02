from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import sys
import socket
print(socket.gethostbyname(socket.gethostname()))

print(sys.platform)

app = FastAPI()

class MyRequest(BaseModel):
	funcao: str
	num1: int
	num2: int

operacoes = ["soma","subtracao","multiplicacao","divisao"]
portas = [8100,8200,8300,8400]
ips = ["soma","subtracao","multiplicacao","divisao"]

@app.post("/")
async def calcular(req: MyRequest):
    if req.funcao not in operacoes:
        return {"message": "Erro: funcao invalida"}
    port = portas[operacoes.index(req.funcao)]
    ip = ips[operacoes.index(req.funcao)]
    response = requests.post("http://" + ip + ":" + str(port) + "/" + req.funcao, headers={'content-type':'application/json'}, data='{"num1":' + str(req.num1) + ',"num2":' + str(req.num2) + '}')
    result = json.loads(response.content.decode("utf-8"))
    return result
