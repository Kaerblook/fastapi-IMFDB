from fastapi import APIRouter

from .routes import game, user

master_router = APIRouter()

master_router.include_router(game.router)
master_router.include_router(user.router)