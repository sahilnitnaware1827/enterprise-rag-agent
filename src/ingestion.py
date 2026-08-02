from src.loader import PDFLoader
from src.chunker import DocumentChunker
from src.embedding import EmbeddingModel
from src.vectorstore import VectorStore


class IngestionPipeline:

    def __init__(self, pdf_path: str):

        self.loader = PDFLoader(pdf_path)

        self.chunker = DocumentChunker()

        self.embedding_model = EmbeddingModel()

        self.vectorstore = VectorStore(
            self.embedding_model.get_embeddings()
        )

    def run(self):

        documents = self.loader.load()

        chunks = self.chunker.split(documents)

        db = self.vectorstore.create(chunks)

        self.vectorstore.save(db)

        return db
    