from fastapi import APIRouter
from services import group_services
router = APIRouter()


@router.get("/health", status_code=200)
async def health():
     return {"message": "Ready"}


@router.get("/groups", status_code=200)
async def groups():
 return group_services.find_all()