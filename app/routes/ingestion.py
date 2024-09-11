from fastapi import APIRouter, HTTPException
from app.models import ComponentIngestion
from app.utils.embeddings import generate_embedding
from app.db.vector_db import add_to_vector_db

router = APIRouter()

@router.post("/ingest/")
async def ingest_component(data: ComponentIngestion):
    embedding = generate_embedding(data.component_code)
    embedding_list = embedding[0]
    # print(embedding_list)
    add_to_vector_db(data.component_name, data.component_code, embedding_list)
    return {"message": "Component ingested successfully"}
