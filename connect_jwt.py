import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from db.config import SECRET_KEY


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # Обработка исключения при истечении срока действия токена
        return 'Token expired'
    except jwt.InvalidTokenError:
        # Обработка исключения при недействительном токене
        return 'Invalid token'


def validate_token(token: str = Depends(decode_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token
