from qdrant_client import models
from qdrant_client.models import PointStruct, ScoredPoint
from typing import List
import uuid 
from .config import init_vector_db
from ..db import COLLECTION_NAME, VECTOR_DIMENSION

client = init_vector_db()

def create_collection_if_not_exists(collection_name: str):
    """Ensure that the collection exists before using it."""

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=VECTOR_DIMENSION, distance=models.Distance.COSINE),
        )
        
        
def add_to_vector_db(component_name: str, component_code: str, embedding: List[float]):
    """Add a new point to the Qdrant collection."""
    create_collection_if_not_exists(COLLECTION_NAME)
    print(f"Adding to DB: {component_name} with embedding: {embedding[:5]}...")
    point_id = str(uuid.uuid4())
    point = PointStruct(
        id=point_id,
        vector=embedding,
        payload={"component_name": component_name, "component_code": component_code}
    )
    client.upsert(collection_name=COLLECTION_NAME, points=[point])

def search_vector_db(query_embedding: List[float], limit: int = 5) -> List[ScoredPoint]:
    """Search for the most similar points to the query embedding in the specified collection."""
    create_collection_if_not_exists(COLLECTION_NAME)
    print(f"Searching with vector: {query_embedding[:5]}...")
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=limit,
        with_payload=True
    )
    return results

# # Example usage
# embedding = [0.1, 0.2, 0.3]  # Example vector
# component_name = "example_component"
# component_code = "const Example = () => <div>Example</div>;"

# # Add to the vector DB
# add_to_vector_db(component_name, component_code, embedding)

# # Search the vector DB
# search_results = search_vector_db(embedding)
# print("Search results:", search_results)
