from fastapi import APIRouter, UploadFile


router = APIRouter()


@router.post('/upload')
def resource(file: UploadFile):
    return { 'file': file }
