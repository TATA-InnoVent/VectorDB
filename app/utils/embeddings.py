# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)

# from transformers import AutoTokenizer, AutoModelForMaskedLM

# tokenizer = AutoTokenizer.from_pretrained("jinaai/jina-embeddings-v2-base-code", trust_remote_code=True)
# model = AutoModelForMaskedLM.from_pretrained("jinaai/jina-embeddings-v2-base-code", trust_remote_code=True)

# def generate_embedding(code: str):
#     inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True)
#     outputs = model(**inputs, output_hidden_states=True)
#     hidden_states = outputs.hidden_states
#     last_hidden_state = hidden_states[-1]

#     mean_embedding = last_hidden_state.mean(dim=1).detach().numpy()

#     flattened_embedding = mean_embedding
#     print(flattened_embedding)
#     print(f"Shape of mean embedding before flattening: {mean_embedding.shape}")
#     print(f"Shape of flattened embedding: {flattened_embedding.shape}")
    
#     return flattened_embedding



import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/jinaai/jina-embeddings-v2-base-code"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def generate_embedding(code: str):
    response = requests.post(API_URL, headers=headers, json={"inputs":[code]})
    return response.json()
	

