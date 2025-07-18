from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.callback import callback_router
from handlers.commands import comand_router
from handlers.fsm_handlers import fsm_router
from handlers.callback import fishing_router

from dotenv import  load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

dp.include_router(comand_router)
dp.include_router(callback_router)
dp.include_router(fsm_router)
dp.include_router(fishing_router)

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())