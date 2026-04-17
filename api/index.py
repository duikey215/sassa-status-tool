from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Ye block Blogger ko Vercel se data lene ki permission dega
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Duniya ki kisi bhi site (Blogger) ko allow karega
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Vercel Engine is Active!"}

@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # Agar detail galat hai toh directly Failed bhejo
        if r.status_code != 200:
            return {"status": "FAILED", "remark": "No record found."}
        return r.json()
    except:
        return {"error": "System Busy"}
