from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Models.UserModel import User
from Security.user_jwt import createToken, validateToken, BearerJWT


routerLogin = APIRouter()


@routerLogin.post('/login', tags=['authentication'])
def login(user: User):
    if user.email == 'enrique.garcia@astrum.com.mx' and user.password == '123':
        token: str = createToken(user.dict())
        print(token)
        return JSONResponse(content=token)

