from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get("/square")
def square_number(x: int = Query(..., ge=0, le=1000)):
    return {"number": x, "square": x ** 2}
