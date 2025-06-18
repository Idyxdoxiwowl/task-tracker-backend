from fastapi import FastAPI, HTTPException, Path
import httpx

app = FastAPI()

async def fetch_external_task(task_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/todos/{task_id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Task not found in external API")
            data = response.json()
            if "title" not in data:
                raise HTTPException(status_code=422, detail="Invalid response format")
            return data
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"External service error: {str(e)}")

@app.get("/external-task/{task_id}")
async def get_external_task(
    task_id: int = Path(..., ge=1, description="ID задачи, должен быть >= 1")
):
    data = await fetch_external_task(task_id)
    return {
        "source": "jsonplaceholder.typicode.com",
        "task_id": task_id,
        "title": data["title"],
        "completed": data["completed"]
    }
