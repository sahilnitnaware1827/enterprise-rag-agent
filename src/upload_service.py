from pathlib import Path
import shutil

from fastapi import UploadFile

from src.ingestion import IngestionPipeline

from uuid import uuid4
from pathlib import Path


from src.logger import logger


class UploadService:

    def __init__(self):
        self.upload_dir = Path("data")
        self.upload_dir.mkdir(exist_ok=True)

    def upload_pdf(self, files: list[UploadFile]):

        uploaded_files = []

        for file in files:

            logger.info(f"Uploading file: {file.filename}")    

            if file.content_type != "application/pdf":
                logger.error(f"Invalid file type: {file.filename}")
                raise ValueError("Only PDF files are allowed.")

            if not file.filename:
                logger.error("Uploaded file has no filename.")
                raise ValueError("Filename is missing.")

            extension = Path(file.filename).suffix

            filename = f"{uuid4()}{extension}"

            file_path = self.upload_dir / filename

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
                logger.info(f"File saved: {filename}")


            logger.info(f"Starting ingestion: {file.filename}")
            pipeline = IngestionPipeline(pdf_path=str(file_path))
            pipeline.run()
            logger.info(f"Ingestion completed: {file.filename}")




            uploaded_files.append(file.filename)



        logger.info(f"{len(uploaded_files)} file(s) uploaded successfully.")

        return {
            "message": "Files uploaded and processed successfully.",
            "files": uploaded_files
        }
    