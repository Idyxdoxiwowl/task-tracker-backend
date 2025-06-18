import httpx
from fastapi import FastAPI

app = FastAPI()

@app.post("/simulate-post")
async def simulate_post():
    payload = {"title": "Foo", "body": "Bar", "userId": 1}
    async with httpx.AsyncClient() as client:
        response = await client.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        return {
            "status_code": response.status_code,
            "response_data": response.json()
        }
