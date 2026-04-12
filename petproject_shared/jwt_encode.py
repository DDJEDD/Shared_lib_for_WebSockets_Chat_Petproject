import jwt
from datetime import datetime, timedelta, timezone


class JWTEncode:
    """
    JWTEncode is a class that encodes JWT tokens
    """
    def __init__(self, secret_key, algorithm):
        self.secret_key = secret_key
        self.algorithm = algorithm
    def create_token(self,payload) -> str:
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def create_access_token(self,user_id, session_id, expires_in:int) -> str:
        return self.create_token({"sub": session_id, "user_id":user_id ,
                                  "exp": datetime.now(timezone.utc)+ timedelta(minutes=expires_in)})

    def create_refresh_token (self,session_id, expires_in:int) -> str:
        return self.create_token({"sub": session_id,
                                  "exp": datetime.now(timezone.utc)+ timedelta(days=expires_in)})
