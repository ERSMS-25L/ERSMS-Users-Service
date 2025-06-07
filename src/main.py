from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Fake User", "email": "test@example.com"}
