# create db to store in vectordb 

from langchain_community.vectorstores import FAISS

class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model


    # to create embedding from chunks 
    def create(self, chunks):
        vectorstore = FAISS.from_documents(
            documents = chunks,
            embedding = self.embedding_model
        )

        return vectorstore


    # to add in to old database
    def add_documents(self, vectorstore, chunks):

        vectorstore.add_documents(chunks)

        return vectorstore


    # to save the embeddings to local database file 
    def save(self, vectorstore, path= 'db'):
        vectorstore.save_local(path)



    # to load local stores database
    def load(self, path= 'db'):
        return FAISS.load_local(
            folder_path = path,
            embeddings = self.embedding_model,
            allow_dangerous_deserialization = True
        )
    