from fastapi import FastAPI

app = FastAPI(
    title="InternRadar AI",
    description="AI-powered internship discovery and recommendation platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "InternRadar AI",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }