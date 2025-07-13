import random
from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from handlers.game_files import fishes_list
from handlers.game_files import weith_list
from handlers.game_files import ylow_list

callback_router = Router()

@callback_router.callback_query(F.data == "query")
async def get_query(callback: CallbackQuery):
    q_message = "для чего вообще эта кнопка?"
    await callback.answer(text=q_message)

@callback_router.callback_query(F.data == "help")
async def get_help(callback: CallbackQuery):
    help_message = "нужен совет рыбак?"
    await callback.answer(text=help_message)

@callback_router.callback_query(F.data == "на рыбалку!")
async def get_fish(callback: CallbackQuery):
    rand_weith = random.choice(weith_list)
    random_fish = random.choice(fishes_list)
    ylow_fraza = random.choice(ylow_list)
    await callback.message.answer(text=f"И у тебя на крючке...{random_fish}, {rand_weith}kg")
    await callback.answer(text=ylow_fraza)
#    await asyncio.sleep(60)