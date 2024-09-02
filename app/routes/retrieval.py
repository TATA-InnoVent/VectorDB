from fastapi import APIRouter, HTTPException
from app.models import Query
from app.utils.embeddings import generate_embedding
from app.db.vector_db import search_vector_db

router = APIRouter()

@router.post("/retrieve/")
async def retrieve_component(query: Query):
    query_embedding = generate_embedding(query.query_text)
    embedding_list = query_embedding.tolist()[0]
    results = search_vector_db(embedding_list)

    if not results:
        raise HTTPException(status_code=404, detail="No matching component found")
    
    print(results)
    best_match = results[0]
    return {
        "component_id": best_match.id,
        "component_name": best_match.payload["component_name"],
        "component_code": best_match.payload["component_code"]
    }
