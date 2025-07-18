import time
from aiogram import BaseMiddleware
from aiogram.types import Message, Update
from collections import defaultdict

CHAT_BY_DATETIME = dict()

class AntiFloodProgramm(BaseMiddleware):

    def __init__(self, delay: float = 10.0):
        self.delay = delay
        self.last_time = defaultdict(lambda: 0)

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = time.time()

        if current_time - self.last_time[user_id] < self.delay:
            await event.answer("Ожидай рыба еще е клюнула")
            return
        else:
            # upd time last call
            self.last_time[user_id] = current_time
            return await handler(event, data)

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, delay: float = 10):
        self.delay = delay
        self.last_time = defaultdict(lambda: 0)

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.idz
        current_time = time.time()

        if current_time - self.last_time[user_id] < self.delay:
            await event.answer("Подожди немного")
            return
        else:
            self.last_time[user_id] = current_time
            return await handler(event, data)
