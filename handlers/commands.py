from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboards.Inline import start_kb
from keyboards.Inline import start_bd
from keyboards.reply import menu_keyboard

comand_router = Router()

@comand_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Привет рыбак сегодня отличный день, чтобы пловить рыбу!", reply_markup=start_kb)

@comand_router.message(Command("about"))
async def command_about_handler(message: Message):
    text = f"эта мини игра предназначена для ловли рыбы."
    await message.answer(text=text, reply_markup=start_bd)

@comand_router.message(F.text.lower() == "привет")
async def greet(messege: Message):
    await messege.answer(text="Привет, рыбак как идут дела?")

@comand_router.message(F.text.lower() == "пока")
async def say_goodbuy(message: Message):
    await message.answer(text="Увидимся, на следующей рыбалке...")

@comand_router.message(F.text.lower() == "профиль")
async def prof(message: Message):
    await message.answer(text= "вот твой профиль здесь будут появлятся твои рекорды и удочки купленные тобой", reply_markup=menu_keyboard)

@comand_router.message(F.text.lower() == "настройки")
async def nastroiki(message: Message):
    await message.answer(text= "можешь попробовать настроить игру под себя", reply_markup=menu_keyboard)

@comand_router.message(F.sticker)
async def get_sticker_id(message: Message):
   await message.answer("стикер конечно классный ,но я бы не отвлекался от рыбалки ,а то упустишь рыбу своей мечты")

@comand_router.message(Command("help"))
async def command_help_andlers(message: Message):
    text2 = f"Нужен совет?"
    await message.answer(text=text2)

@comand_router.message(F.lower() == "трофеи")
async def trofes(message: Message):
    await message.answer(text=f"  ")

@comand_router.message()
async def echo_message(message: Message) -> None:

    try:
        await message.reply(text=message.text)
    except TypeError:
        await message.answer(text="Хорошая попытка!")
