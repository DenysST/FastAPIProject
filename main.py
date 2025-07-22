from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test-endpoint")
async def test_endpoint():
    return {"message": "This is a test endpoint."}


@app.get("/health-check")
async def health_check():
    return {"status": "ok"}
