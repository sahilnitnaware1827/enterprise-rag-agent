from src.loader import PDFLoader
from src.chunker import DocumentChunker
from src.embedding import EmbeddingModel
from src.vectorstore import VectorStore
from pathlib import Path
from src.logger import logger


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

        logger.info(f"Loaded {len(documents)} pages from PDF.")

        chunks = self.chunker.split(documents)

        logger.info(f"Created {len(chunks)} chunks.")

        db_path = Path("db")


        logger.info("Checking existing FAISS database...")

        if db_path.exists():

            db = self.vectorstore.load()

            logger.info("Loaded existing FAISS database.")

            db = self.vectorstore.add_documents(
                db,
                chunks
            )

            logger.info("Added new document chunks to existing database.")

        else:

            db = self.vectorstore.create(chunks)

            logger.info("Created new FAISS database.")

        self.vectorstore.save(db)

        logger.info("FAISS database saved successfully.")

        return db
    