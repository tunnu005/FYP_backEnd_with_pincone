from typing import Union
from fastapi import FastAPI
# from pinecone import Pinecone
from fastapi.middleware.cors import CORSMiddleware

from queryprosses1.queryprosses1 import prosess_query
app = FastAPI()


# Define the origins you want to allow
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
     "http://127.0.0.1:5174",
      "http://localhost:5174",
    # You can add more allowed origins here
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of origins that should be allowed
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greet")
async def greet(name: str = "query"):
    return {"message": f"Hello, {name}!"}

@app.get("/querys")
async def querys(query: str = "query"):
    result = prosess_query(query)
    return {"message": result}







