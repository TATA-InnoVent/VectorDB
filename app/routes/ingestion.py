from fastapi import APIRouter, HTTPException
from app.models import ComponentIngestion
from app.utils.embeddings import generate_embedding
from app.db.vector_db import add_to_vector_db

router = APIRouter()

@router.post("/ingest/")
async def ingest_component(data: ComponentIngestion):
    try:
        embedding = generate_embedding(data.component_code)
        if len(embedding) < 1:
            raise ValueError("Empty embedding returned")
        embedding_list = embedding[0]
        add_to_vector_db(data.component_name, data.component_code, embedding_list)
        return {"message": "Component ingested successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
