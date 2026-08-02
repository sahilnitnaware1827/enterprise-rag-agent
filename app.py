# Create entry point 

from fastapi import FastAPI

app = FastAPI(
    title = "Enterprise RAG Agent",
    description = "This is an API for the Enterprise RAG Agent, which is designed to provide relevant information and insights based on user queries. The API leverages advanced retrieval techniques to access and present data from various sources.",
    version = "0.1.0"
)

@app.get("/")
def home():

    return {
        "Meassage": "Welcome to the Enterprise RAG Agent API"
    }
