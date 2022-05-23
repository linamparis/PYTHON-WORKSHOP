from fastapi import APIRouter

router = APIRouter()


@router.get("/health", status_code=200)
async def health():
     return {"message": "Ready"}
@router.get("/groups", status_code=200)
async def groups():
     return {"message": "Ready"}