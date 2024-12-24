from pinecone import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import numpy as np
from dotenv import load_dotenv
import os
import google.generativeai as gemini_ai


load_dotenv()


gemini_api_key = os.environ.get('API_KEY_GEMINI')
openai_api_key = os.environ.get('API_KEY_OPENAI')

gemini_ai.configure(api_key=gemini_api_key)

api_key_pinecone = os.environ.get('API_KEY_PINCONE')
# Initialize Pinecone with API key
pc = Pinecone(api_key=api_key_pinecone)  # Replace with your actual API key

# Define index name
index_name = "data-of-cse"

# Initialize HuggingFace model for embeddings
model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")
embedding_function = model.embed_query

index = pc.Index(index_name)


def queryProsses(query):
    # Assuming 'model' and 'index' are already defined properly
    query_vector = model.embed_query(query)
    print("vectors for query: ", query_vector)
    # Perform the query on Pinecone (search for similar vectors)
   
    response = index.query(vector=query_vector, top_k=10, include_metadata=True)
        
        # Inspect the response structure
        # print(response)  # Uncomment this to view the structure
    for match in response["matches"]:
         print(match['metadata']['data'])
        # Access the 'matches' and extract the metadata
    retrieved_documents = [match['metadata']['data'] for match in response['matches']]
    print(len(retrieved_documents))
    return retrieved_documents
   
    


def generate_response(prompt):
    model = gemini_ai.GenerativeModel('gemini-1.5-pro')

    try:
        response = model.generate_content(prompt)

    # print("Response:", response)
        
        # Check if candidates are available
        if not response.candidates:
            return "No response available."

        # Check if content and parts are available
        if not response.candidates[0].content.parts:
            return "No content parts available."

        print('Gemini response:', response.candidates[0].content.parts)
        return response.candidates[0].content.parts[0].text
    except : 
        return ["Error in Responce generation. please try after sometime again"]


def prosess_query(user_query):
    retrieved_documents = queryProsses(user_query)
    
    prompt = f"User Query: {user_query}\n\nRelevant Information:\n{retrieved_documents}\n\nBased on the above information, please provide a response to the user's query just like how human will response to this query.\n\n if the answer is not there in document just say i don't have information about that please contact CSE Department Office for that."

    # Generate response using the generative model
    response = generate_response(prompt)
    return response

# while True:
#     user_query = input("Enter your query: ")
   
#     # Check if any of the stop words are in the query
#     if any(word in user_query.lower() for word in ['bye bye', 'quit', 'leave', 'stop']):
#         print("Exiting...")
#         break

#     # Process the query
#     retrieved_documents = queryProsses(user_query)
    
#     prompt = f"User Query: {user_query}\n\nRelevant Information:\n{retrieved_documents}\n\nBased on the above information, please provide a response to the user's query just like how human will response to this query.\n\n if the answer is not there in document just say i don't have information about that please contact CSE Department Office for that."

#     # Generate response using the generative model
#     response = generate_response(prompt)

#     print("Response:", response)






