# create graph

from langchain.agents import create_agent

from src.llm import LLM
from src.embedding import EmbeddingModel
from src.vectorstore import VectorStore
from src.retrieval import DocumentRetriever
from src.tools import RAGTool


embedding = EmbeddingModel()

vectorstore = VectorStore(
    embedding.get_embeddings()
)

db = vectorstore.load()

retriver = DocumentRetriever(db).get_retriever()

search_tool = RAGTool(retriver).get_tool()

llm = LLM().get_model()

agent = create_agent(
    model = llm,
    tools = [search_tool],
    system_prompt= """
        You are an Enterprise Knowledge Assistant.

        Always search the knowledge base before answering.

        If the answer is not found in the documents,
        say

        'I couldn't find this information in the knowledge base.'

        Never make up information. 
    """
)