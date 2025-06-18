from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {"1": "Task A", "2": "Task B"}

@app.get("/task/{task_id}")
def get_task(task_id: str):
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task_id, "title": fake_db[task_id]}
