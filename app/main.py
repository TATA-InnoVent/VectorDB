from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ingestion, retrieval
from fastapi.responses import HTMLResponse
import os

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

@app.get("/", response_class=HTMLResponse)
async def root():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "main.html")
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
