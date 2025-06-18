from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/inspect")
async def inspect_request(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "client": request.client.host,
        "headers": dict(request.headers)
    }
