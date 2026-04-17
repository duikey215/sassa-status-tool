from fastapi import FastAPI
import requests

app = FastAPI()

# Agar galti se koi seedha is file par aaye, toh error na aaye
@app.get("/")
def read_root():
    return {"message": "Engine is running. Go to home page."}

@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # Agar detail galat hai ya server "Not Found" bole toh FAILED bhej do
        if r.status_code != 200:
            return {"status": "FAILED", "remark": "No record found."}
        return r.json()
    except:
        return {"error": "System Busy"}
