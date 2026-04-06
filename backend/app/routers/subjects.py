from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_subjects():
    return {"message": "Subjects endpoint - to be implemented"}
