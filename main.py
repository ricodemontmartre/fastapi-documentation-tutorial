from fastapi import FastAPI

app = FastAPI()


@app.get("/")
# async def root():
def root():
    return {"message": "Hello World"}