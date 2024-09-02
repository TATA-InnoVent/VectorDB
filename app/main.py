from fastapi import FastAPI
from app.routes import ingestion, retrieval

app = FastAPI()

# Include routes from ingestion and retrieval modules
app.include_router(ingestion.router)
app.include_router(retrieval.router)

@app.get("/")
async def root():
    return {"message": "FastAPI server for Vector DB with React component retrieval"}
