from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

# 1. Home Page Route (Ye index.html ko browser me dikhayega)
@app.get("/", response_class=HTMLResponse)
def show_ui():
    # Vercel par file ka sahi rasta (path) dhoondhne ka logic
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(base_dir, "index.html")
    
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        try:
            # Fallback path
            with open("index.html", "r", encoding="utf-8") as f:
                return f.read()
        except:
            return "<h1>Error: index.html file missing. Kripya check karein.</h1>"

# 2. SASSA API Route (Ye data fetch karega)
@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        return r.json()
    except:
        return {"error": "Server Busy. Try Again."}
