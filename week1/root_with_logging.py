from fastapi import FastAPI, Request, Query
from datetime import datetime
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root(request: Request, name: str = Query("Гость", description="Имя пользователя")):
    client_host = request.client.host
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    logging.info(f"GET / from {client_host} at {current_time}")

    return {
        "message": f"Добро пожаловать, {name}!",
        "api_version": "1.0",
        "server_time": current_time
    }
