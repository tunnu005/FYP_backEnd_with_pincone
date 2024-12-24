# queryprosses1/__init__.py

# Import necessary modules and functions
from .queryprosses1 import prosess_query, queryProsses, generate_response

# Initialization logic
from pinecone import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import numpy as np
from dotenv import load_dotenv
import os
import google.generativeai as gemini_ai


# Load environment variables when the package is initialized
load_dotenv()

# Configure the external services (Gemini AI, Pinecone)
gemini_api_key = os.environ.get('API_KEY_GEMINI')
gemini_ai.configure(api_key=gemini_api_key)

print("Package initialized and external services configured.")
