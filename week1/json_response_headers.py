from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/custom-headers")
def custom_headers():
    data = {"message": "Check headers"}
    headers = {"X-App-Version": "1.0.0", "X-Environment": "development"}
    return JSONResponse(content=data, headers=headers)
