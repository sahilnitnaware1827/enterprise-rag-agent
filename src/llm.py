# Create llm to work with the RAG tool to answer questions based on the knowledge base.

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

class LLM:

    def __init__(self):

        self.llm = init_chat_model(
            model = "gemini-3.5-flash-lite",
            model_provider = "google_genai"
        )

    def get_model(self):

        return self.llm

        