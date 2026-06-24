from fastapi import FastAPI

app = FastAPI(title="MojFakturnik API")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "MojFakturnik"
    }