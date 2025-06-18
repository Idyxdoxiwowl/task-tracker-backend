from fastapi import FastAPI
import asyncio
from datetime import datetime

app = FastAPI()

@app.get("/delay")
async def delayed():
    before = datetime.utcnow().isoformat()
    await asyncio.sleep(2)
    after = datetime.utcnow().isoformat()
    return {"before": before, "after": after}
