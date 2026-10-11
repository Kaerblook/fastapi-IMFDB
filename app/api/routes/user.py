from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.schemas.user import UserCreate, UserRead

from ...core.security import oa2_scheme
from ..dependencies import userDep

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/signup", response_model=UserRead)
async def create_account(user: UserCreate, service: userDep):
    return await service.add(user)

@router.post("/login")
async def login_user(request_form: Annotated[OAuth2PasswordRequestForm, Depends()], service: userDep):

    token = await service.login(request_form.username, request_form.password)

    return {
        "access_token": token,
        "type": "jwt"
    }

@router.get("/dashboard")
async def get_dashboard(token: Annotated[str, Depends(oa2_scheme)]):
    return {
        "token": token,
    }