from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_strategy():
    return {"message": "Strategy endpoint - to be implemented"}
