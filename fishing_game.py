from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.callback import callback_router
from handlers.commands import comand_router

from dotenv import  load_dotenv
import os
import asyncio



load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(comand_router)
dp.include_router(callback_router)

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())