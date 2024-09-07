from qdrant_client import QdrantClient
from ..db import QDRANT_URL, QDRANT_API_KEY

# Initialize Qdrant client
def init_vector_db():
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    return client
