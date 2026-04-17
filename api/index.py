from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/check")
def check_status(id_num: str, phone: str):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://srd.sassa.gov.za/'
    }
    api_url = f"https://srd.sassa.gov.za/sc19/status/{id_num}/{phone}"
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # Agar status code 200 nahi hai toh invalid details
        if r.status_code != 200:
            return {"status": "INVALID", "remark": "No record found for these details."}
        return r.json()
    except:
        return {"error": "SASSA Server is busy. Try again later."}
