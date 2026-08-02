# create retriever to retrieve relevant documents from vectordb

class DocumentRetriever:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def get_retriever(self, search_type: str = "similarity", k: int = 4,):
        
        return self.vectorstore.as_retriever(
            search_type=search_type,
            search_kwargs={"k": k},
        )
    