from fastapi import Request, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials
import jwt
from fastapi.security import HTTPBearer


SECRET_KEY = 'misecret'
ALGORITHM = 'HS256'

def createToken(data: dict) -> str:
    token: str = jwt.encode(payload=data, key=SECRET_KEY, algorithm=ALGORITHM)  # Always the key must save on the environment variable
    return token

def validateToken(token: str) -> dict:
    data: dict = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return data

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['email'] != 'enrique.garcia@astrum.com.mx':
            raise HTTPException(status_code=403, detail='Credenciales incorrectas')