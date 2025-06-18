from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

async def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()

@app.get("/parallel")
async def parallel_requests():
    results = await asyncio.gather(
        fetch_post(1), fetch_post(2), fetch_post(3)
    )
    return results
