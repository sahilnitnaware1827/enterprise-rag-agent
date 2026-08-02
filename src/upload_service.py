from pathlib import Path
import shutil

from fastapi import UploadFile

from src.ingestion import IngestionPipeline

from uuid import uuid4
from pathlib import Path


class UploadService:

    def __init__(self):
        self.upload_dir = Path("data")
        self.upload_dir.mkdir(exist_ok=True)

    def upload_pdf(self, files: list[UploadFile]):

        uploaded_files = []

        for file in files:

            if file.content_type != "application/pdf":
                raise ValueError("Only PDF files are allowed.")

            if not file.filename:
                raise ValueError("Filename is missing.")

            extension = Path(file.filename).suffix

            filename = f"{uuid4()}{extension}"

            file_path = self.upload_dir / filename

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            pipeline = IngestionPipeline(pdf_path=str(file_path))
            pipeline.run()

            uploaded_files.append(file.filename)

        return {
            "message": "Files uploaded and processed successfully.",
            "files": uploaded_files
        }
    