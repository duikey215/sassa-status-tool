from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    # Real SASSA API Endpoint
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        return r.json()
    except:
        return {"error": "Server Busy. Try Again."}
