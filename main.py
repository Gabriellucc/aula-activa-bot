from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Aula Activa online"}

@app.get("/webhook")
def verify(mode: str, challenge: str, verify_token: str):
    if verify_token == "aula_activa_token":
        return challenge
    return "Error"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print(data)
    return {"status": "received"}
