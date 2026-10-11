from datetime import date, datetime, timedelta

import jwt
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.api.schemas.user import UserCreate

from ..config import security_setting
from ..database.models import User

pass_context = PasswordHash.recommended()

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, credentials: UserCreate) -> User:
        user = User(
            **credentials.model_dump(exclude=["password"]),
            created_at=date.today(),
            password_hash=pass_context.hash(credentials.password),
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def login(self, email, password) -> str:
        result = await self.session.execute(select(User).where(User.email == email))

        user = result.scalar()

        if user is None or not pass_context.verify(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="That email or password is incorrect"
            )

        token = jwt.encode(
            payload={"user": {
                "name": user.username,
                "email": user.email,
            },
            "exp": datetime.now() + timedelta(days=1.5),
            },
            algorithm=security_setting.JWT_ALGORITHM,
            key=security_setting.JWT_SECRET,
        )        

        return token

        

        
    