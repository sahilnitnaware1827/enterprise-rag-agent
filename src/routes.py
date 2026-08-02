from fastapi import APIRouter

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
