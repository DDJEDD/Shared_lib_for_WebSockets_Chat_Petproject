class RedisService:
    def __init__(self, redis_service):
        self.r = redis_service

    async def set_user(self, user_id: int, username: str, login: str = None):
        data = {"username": username}
        if login:
            data["login"] = login
            await self.r.set(f"login:{login}", user_id)

        await self.r.set(f"username:{username}", user_id)
        await self.r.hset(f"user:{user_id}", mapping=data)

    async def check_user_exists(self, user_id: int):
        return await self.r.exists(f"user:{user_id}")

    async def get_user(self, user_id: int):
        return await self.r.hgetall(f"user:{user_id}")

    async def get_id_by_login(self, login: str):
        return await self.r.get(f"login:{login}")

    async def update_username(self, user_id: int, old_username: str, new_username: str):
        if old_username:
            await self.r.delete(f"username:{old_username}")

        await self.r.set(f"username:{new_username}", user_id)

        if await self.r.exists(f"user:{user_id}"):
            await self.r.hset(f"user:{user_id}", "username", new_username)