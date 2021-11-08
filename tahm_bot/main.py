import requests
import json
from fastapi import FastAPI, Request


app = FastAPI()

TOKEN = ''  # Telegram Bot API Key

def send_mess(chat_id,mess:str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = json.dumps({
    "chat_id": chat_id,
    "text": mess
    })
    print(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


@app.post("/webhook")
async def recWebHook(req: Request):
    body = await req.json()
    id = body['message']['chat']['id']
    sender_text = body['message']['text']
    send_mess(id,mess="mèo meo meo mèo meo")
