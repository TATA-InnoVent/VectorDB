
---

# VectorDB Integration with FastAPI

FastAPI server integrated with the Qdrant vector database for storing and retrieving React component codes based on embeddings.

## Project Structure

```
vectordb/
├── app/
│   ├── __init__.py
│   ├── main.py
|   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ingestion.py
│   │   └── retrieval.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── embeddings.py
|   ├── db/
│   │   ├── __init__.py
│   │   ├── vector_db.py
│   └── └── config.py

├── .env
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd vectordb
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Qdrant API key and URL:

   ```
   QDRANT_API_KEY=<your_qdrant_api_key>
   QDRANT_URL=<your_qdrant_url>
   ```

## Running the Application

1. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

2. **Run the FastAPI server:**

   ```bash
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

3. **Open your browser and navigate to:**

   ```
   http://localhost:8000
   ```

   You can access the API documentation at `/docs`.

## Docker Qdrant Setup
**Pull the Qdrant Docker Image:**
   ```
   docker pull qdrant/qdrant
   ```
**Run the Qdrant Container:**
   ```
   docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
   ```
   Qdrant will be running on port 6333 on localhost.
   
## API Endpoints

### Data Ingestion

- **POST /ingest**

  Upload component code and store its embedding in the Qdrant vector database.

  **Request Body:**

  ```json
  {
    "component_name": "MyComponent",
    "component_code": "const MyComponent = () => <div>Hello</div>;"
  }
  ```

### Component Retrieval

- **POST /retrieve**

  Retrieve the most relevant component code based on a provided prompt.

  **Request Body:**

  ```json
  {
    "prompt": "Find me a React component for a greeting message."
  }
  ```

## Code Explanation

- **`app/main.py`**: Entry point for the FastAPI application.
- **`app/routes/ingestion.py`**: Handles data ingestion and stores embeddings in Qdrant.
- **`app/routes/retrieval.py`**: Handles retrieval of component codes based on embeddings.
- **`app/utils/embeddings.py`**: Contains functions for generating and managing embeddings.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a clear description of the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---