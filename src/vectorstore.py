# create db to store in vectordb 

from langchain_community.vectorstores import FAISS

class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create(self, chunks):
        vectorstore = FAISS.from_documents(
            documents = chunks,
            embedding = self.embedding_model
        )

        return vectorstore

    def save(self, vectorstore, path= 'db'):
        vectorstore.save_local(path)

    def load(self, path= 'db'):
        return FAISS.load_local(
            folder_path = path,
            embeddings = self.embedding_model,
            allow_dangerous_deserialization = True
        )
    