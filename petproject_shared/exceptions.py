
class JWTError(Exception):
    pass
class RedisError(Exception):
    pass

class UserAlreadyExists(RedisError):
    pass
class UserNotFound(RedisError):
    pass
class TokenExpiredError(JWTError):
    pass