from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ingestion, retrieval

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from ingestion and retrieval modules
app.include_router(ingestion.router)
app.include_router(retrieval.router)

@app.get("/")
async def root():
    return {"message": "FastAPI server for Vector DB with React component retrieval"}
