from fastapi.security import OAuth2PasswordBearer

oa2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")