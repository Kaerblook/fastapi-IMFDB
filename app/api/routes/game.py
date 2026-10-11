from fastapi import APIRouter, HTTPException, status

from ..dependencies import gameDep
from app.api.schemas.game import GameCreate, GameRead, GameUpd

router = APIRouter(prefix="/game", tags=["Game"])

@router.get("/", response_model=GameRead)
async def get_game(id: int, service: gameDep):
    game = await service.get(id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="That game does not exist"
        )

    return game

@router.post("/", response_model=None)
async def create_game(game: GameCreate, service: gameDep):
    return await service.add(game)

@router.patch("/", response_model=GameRead)
async def update_game(id: int, game_update: GameUpd, service: gameDep):
    update = game_update.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No values provided for difficulty, is complete, or number of attempts"
        )

    game = await service.update(id, update)

    return game

@router.delete("/")
async def delete_game(id: int, service: gameDep):
    await service.delete(id)

    return {"detail": f"The game with id = {id} has been deleted"}