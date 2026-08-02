# Create search tool to load documents from a PDF file, chunk the documents, embed the chunks, and store the embeddings in a vector database for retrieval.

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

            return "\n\n".join(
                doc.page_content for doc in docs
            )

        return search_documents
        