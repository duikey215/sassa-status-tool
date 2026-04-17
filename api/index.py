from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # Agar server 200 OK na de, toh sidha Failed
        if r.status_code != 200:
            return {"status": "FAILED", "remark": "No record found."}
        return r.json()
    except:
        return {"error": "System Busy"}
