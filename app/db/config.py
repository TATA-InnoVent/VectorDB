from qdrant_client import QdrantClient
from ..db import QDRANT_URL, QDRANT_PORT

# Initialize Qdrant client
def init_vector_db():
    client = QdrantClient(host=QDRANT_URL, port=QDRANT_PORT)
    return client
