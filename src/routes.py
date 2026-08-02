from fastapi import APIRouter
from fastapi import File, UploadFile, HTTPException
from src.upload_service import UploadService


router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Enterprise RAG Agent"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


upload_service = UploadService()

@router.post("/upload")
def upload_files(file: UploadFile = File(...)):

    try:

        return upload_service.upload_pdf(file)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    