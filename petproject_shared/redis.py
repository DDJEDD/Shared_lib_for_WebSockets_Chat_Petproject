import redis.asyncio as redis

class RedisService:
    def __init__(self, host, port, db):

        self.r = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    async def set_user(self, user_id: int, username: str, login: str = None):
        data = {"username": username}
        if login:
            data["login"] = login
        await self.r.set(f"username:{username}", user_id)
        await self.r.hset(f"user:{user_id}", mapping=data)

    async def check_user_exists(self, user_id: int):
        return await self.r.exists(f"user:{user_id}")

    async def get_user(self, user_id: int):
        data = await self.r.hgetall(f"user:{user_id}")
        return data
    async def get_id_by_username(self, username: str):
        return await self.r.get(f"username:{username}")