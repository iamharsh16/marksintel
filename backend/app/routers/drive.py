from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_drive():
    return {"message": "Drive endpoint - to be implemented"}
