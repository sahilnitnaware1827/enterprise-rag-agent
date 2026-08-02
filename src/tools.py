# Create search tool to load documents from a PDF file, chunk the documents, embed the chunks, and store the embeddings in a vector database for retrieval.

from pathlib import Path
from langchain.tools import tool


class RAGTool:

    def __init__(self, retriever):
        self.retriever = retriever

    def get_tool(self):

        @tool
        def search_documents(query: str) -> str:
            '''
                searching the knowledge base for relevant information to answer the query.
            '''        

            docs = self.retriever.invoke(query)

            formatted_docs = []

            for doc in docs:

                source = Path(doc.metadata.get("source", "Unknown")).name

                page = doc.metadata.get("page", "Unknown")

                content = doc.page_content

                formatted_docs.append(
                    f"""
                    Content:
                    {content}

                    Source:
                    {source}

                    Page:
                    {page}"""
                )

            return "\n\n----------------\n\n".join(formatted_docs)

        return search_documents
        