# create graph

from langchain.agents import create_agent

from src.llm import LLM
from src.embedding import EmbeddingModel
from src.vectorstore import VectorStore
from src.retrieval import DocumentRetriever
from src.tools import RAGTool
from src.prompts import RAG_SYSTEM_PROMPT


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
    system_prompt= RAG_SYSTEM_PROMPT
)