from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import sys
import socket
import os

ip_address = str(os.environ.get("IP_ADDRESS"))
port_soma = str(os.environ.get("PORT_SOMA"))
port_sub = str(os.environ.get("PORT_SUB"))
port_multi = str(os.environ.get("PORT_MULTI"))
port_div = str(os.environ.get("PORT_DIV"))

app = FastAPI()

class MyRequest(BaseModel):
  num1: int
  num2: int
    
@app.post("/soma")
async def soma(req : MyRequest):
	response = requests.post(ip_address + ":" + port_soma, headers={'Content-type':'application/json'},data=req.json())
	return json.loads(response.content)
	
@app.post("/sub")
async def sub(req : MyRequest):
	response = requests.post(ip_address + ":" + port_sub, headers={'Content-type':'application/json'},data=req.json())
	return json.loads(response.content)
	
@app.post("/multi")
async def multi(req : MyRequest):
	response = requests.post(ip_address + ":" + port_multi, headers={'Content-type':'application/json'},data=req.json())
	return json.loads(response.content)
	
@app.post("/div")
async def div(req : MyRequest):
	response = requests.post(ip_address + ":" + port_div, headers={'Content-type':'application/json'},data=req.json())
	return json.loads(response.content)
