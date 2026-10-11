from datetime import datetime
from enum import Enum

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class Difficulty(str, Enum):

    easy = "easy"
    medium = "medium"
    hard = "hard"

class Game(SQLModel, table=True):

    game_id: int = Field(default=None, primary_key=True)
    is_complete: bool
    num_attempts: int
    difficulty: Difficulty
    date_played: datetime

class User(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    username: str
    email: EmailStr
    password_hash: str
