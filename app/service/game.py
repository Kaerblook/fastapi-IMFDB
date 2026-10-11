from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.game import GameCreate
from app.database.models import Game

class GameService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int) -> Game:
        return await self.session.get(Game, id)

    async def add(self, create_game: GameCreate) -> Game:
        new_game = Game(
            **create_game.model_dump(),
            date_played=datetime.now(timezone.utc)
        )

        self.session.add(new_game)
        await self.session.commit()
        await self.session.refresh(new_game)

        return new_game

    async def update(self, id: int, game_update: dict) -> Game:
        game = await self.get(id)
        game.sqlmodel_update(game_update)

        self.session.add(game)
        await self.session.commit()
        await self.session.refresh(game)

        return game

    async def delete(self, id: int) -> None:
        await self.session.delete(
            await self.get(id)
        )
        await self.session.commit()