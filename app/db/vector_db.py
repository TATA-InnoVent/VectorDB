from qdrant_client import models
from qdrant_client.models import PointStruct, ScoredPoint
from typing import List
import uuid 
from .config import init_vector_db
from ..db import COLLECTION_NAME, VECTOR_DIMENSION

client = init_vector_db()

TEMPLATE_COMPONENT_CODE = (
    "const {component_name} = () => { return <div>This is a template component for {component_name}.</div>; };"
)

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


def search_vector_db(query_embedding: List[float], component_name: str, limit: int = 5) -> List[models.ScoredPoint]:
    """Search for the most similar points to the query embedding with a filter on component_code."""
    
    create_collection_if_not_exists(COLLECTION_NAME)
    print(f"Searching with vector: {query_embedding[:5]} and component code: {component_name}...")

    # Define the filter for component_code
    keyword_filter = models.Filter(
        must=[
            models.FieldCondition(
                key="component_name",
                match=models.MatchValue(value=component_name)
            )
        ]
    )

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,  
        query_filter=keyword_filter,
        limit=limit,
        with_payload=True
    )
    if not results:
        print("No results found, returning template component code...")
        return {
            "component_name": component_name,
            "component_code": TEMPLATE_COMPONENT_CODE.replace("{component_name}", component_name)
        }
        
    formatted_result = {
        "component_name": results[0].payload["component_name"],
        "component_code": results[0].payload["component_code"]
    }
    return formatted_result
    
# # Example usage
# embedding = [0.1, 0.2, 0.3]  # Example vector
# component_name = "example_component"
# component_code = "const Example = () => <div>Example</div>;"

# # Add to the vector DB
# add_to_vector_db(component_name, component_code, embedding)

# # Search the vector DB
# search_results = search_vector_db(embedding)
# print("Search results:", search_results)
