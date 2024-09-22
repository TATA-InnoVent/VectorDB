from fastapi import APIRouter, HTTPException
from app.models import Query
from app.utils.embeddings import generate_embedding
from app.db.vector_db import search_vector_db

router = APIRouter()

@router.post("/retrieve/")
async def retrieve_component(query: Query):
    try:
        query_embedding = generate_embedding(query.query_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating embedding: {str(e)}")

    try:
        print(query_embedding)
        if len(query_embedding) < 1:
            raise ValueError("Empty embedding returned")
        embedding_list = query_embedding[0]
    except IndexError:
        raise HTTPException(status_code=400, detail="Invalid embedding format")

    try:
        results = search_vector_db(embedding_list, query.component_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching vector database: {str(e)}")

    if not results:
        raise HTTPException(status_code=404, detail="No matching component found")

    try:
        if not results:
            raise ValueError("No results found")
        return results
    except (IndexError, KeyError) as e:
        raise HTTPException(status_code=500, detail=f"Error processing results: {str(e)}")
