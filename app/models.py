from pydantic import BaseModel

class ComponentIngestion(BaseModel):
    component_name: str
    component_code: str

class Query(BaseModel):
    query_text: str
