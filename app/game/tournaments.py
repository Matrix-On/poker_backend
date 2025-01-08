from fastapi import APIRouter

router = APIRouter()

@router.get("/tournaments")
async def get_tournaments():
    return ["tour1", "tour2", "tour3"]
