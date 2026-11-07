from fastapi import FastAPI

app = FastAPI(
    title="PaperDiff API",
    description="Research Paper Comparison and Gap Identification",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to PaperDiff API",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}