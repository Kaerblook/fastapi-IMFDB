from datetime import datetime

from pydantic import BaseModel, Field

from app.database.models import Difficulty



class GameCreate(BaseModel):
    is_complete: bool = Field(default=False)
    num_attempts: int
    difficulty: Difficulty


class GameRead(GameCreate):
    date_played: datetime # type: ignore



class GameUpd(BaseModel):
    is_complete: bool | None = Field(default=None)
    num_attempts: int | None = Field(default=None)
    difficulty: Difficulty | None = Field(default=None)