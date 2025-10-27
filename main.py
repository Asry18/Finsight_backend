from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Next.js) to call backend APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, use specific domain instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello from backecn-FastAPI!"}
