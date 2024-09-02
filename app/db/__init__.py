import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the environment variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_PORT = os.getenv("QDRANT_PORT")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
