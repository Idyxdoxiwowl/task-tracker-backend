from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/headers")
async def get_headers(request: Request):
    return {
        "User-Agent": request.headers.get("user-agent"),
        "Accept": request.headers.get("accept")
    }
