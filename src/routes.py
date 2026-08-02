from fastapi import APIRouter
from fastapi import File, UploadFile, HTTPException
from src.upload_service import UploadService

from pydantic import BaseModel
from src.chat_service import ChatService

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




''' ADD UPLOAD SERVICE ENDPOINT '''
upload_service = UploadService()

@router.post("/upload")
def upload_files(file: UploadFile = File(...)):

    try:

        return upload_service.upload_pdf(file)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    


''' ADD CHAT SERVICE ENDPOINT '''
chat_service = ChatService()    # chat_service is an object of ChatService class which is used to handle user queries and generate responses


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    answer = chat_service.ask(request.question)     # ask is a function of ChatService class which takes a question as input and returns the answer 

    return {"answer": answer}
