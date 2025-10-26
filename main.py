from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/api/appointments")
def get_appointments():
    return [
        {"id": 1, "customer": "Asry", "status": "Pending"},
        {"id": 2, "customer": "Sam", "status": "Confirmed"},
    ]
