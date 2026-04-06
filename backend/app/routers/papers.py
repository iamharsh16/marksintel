from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_papers():
    return {"message": "Papers endpoint - to be implemented"}
