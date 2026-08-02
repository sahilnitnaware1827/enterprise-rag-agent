# Create a file to chunk data from a PDF file and save it to a new file. The new file will be used for embedding and retrieval.

from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100) -> None:
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, documents):
        return self.splitter.split_documents(documents)
    