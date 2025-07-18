from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="профиль🗂️")],
        [KeyboardButton(text="Настройки⚙️")]
    ],
    resize_keyboard=True
)