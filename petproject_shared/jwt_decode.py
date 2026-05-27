import jwt
from .exceptions import TokenExpiredError, AccessTokenExpired

class JWTDecode:
    """
    JWTDecode is a class that decodes JWT tokens
    """
    def __init__(self, secret_key, algorithm):
        self.secret_key = secret_key
        self.algorithm = algorithm
    def decode_token(self, token, verify_exp: bool):
        try:
            return jwt.decode(token,self.secret_key,
                              algorithms=[self.algorithm],
                              options={"verify_exp": verify_exp}, )
        except jwt.ExpiredSignatureError:
            raise TokenExpiredError

    def get_user_id(self,payload) -> int:
        return int(payload.get("user_id"))

    def get_session_id(self,payload) -> str:
        return payload.get("sub")
    def get_current_user(self, access_token: str):
        try:
            payload = self.decode_token(access_token, True)
        except TokenExpiredError:
            raise AccessTokenExpired()
        user_id = self.get_user_id(payload)
        return user_id

