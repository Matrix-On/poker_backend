from fastapi import APIRouter

router = APIRouter()

@router.get("/active_games")
async def get_tournaments():
    return { "games" : [{"id": 1, "name": "first"}, {"id": 2, "name": "last"}, {"id": 5, "name": "five"}]}
