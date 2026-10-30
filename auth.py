from datetime import datetime, timedelta
import jwt

SECRET_KEY = "your-secret-key"

def login(email: str, password: str) -> dict:
    """Authenticate user and return a JWT token."""
    user = authenticate(email, password)
    token = generate_jwt(
        user_id=user.id,
        expires_in=3600, # 1 hour
    )
    return {"token": token, "expires_in": 3600}

def refresh(current_token: str) -> dict:
    """Refresh a valid token with a new 1-hour expiry."""
    payload = decode_jwt(current_token)
    new_token = generate_jwt(
        user_id=payload["user_id"],
        expires_in=3600, # 1 hour
    )
    return {"token": new_token, "expires_in": 3600}

def generate_jwt(user_id: str, expires_in: int) -> str:
    exp = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode({"user_id": user_id, "exp": exp}, SECRET_KEY, algorithm="HS256")

def decode_jwt(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

def authenticate(email: str, password: str):
    # stub
    ...
