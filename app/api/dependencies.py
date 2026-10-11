from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.service.game import GameService
from app.service.user import UserService

sessionDep = Annotated[AsyncSession, Depends(get_session)]

def get_game_service(session: sessionDep):
    return GameService(session)

def get_user_service(session: sessionDep):
    return UserService(session)


userDep = Annotated[UserService, Depends(get_user_service)]
gameDep = Annotated[GameService, Depends(get_game_service)]