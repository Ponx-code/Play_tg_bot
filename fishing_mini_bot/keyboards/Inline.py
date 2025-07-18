from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
     inline_keyboard=[
         [InlineKeyboardButton(text="отвлечься?", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")],
         [InlineKeyboardButton(text="изменить профиль", callback_data="query")],
         [InlineKeyboardButton(text="на рыбалку!", callback_data="на рыбалку!")]
     ]
 )


start_bd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отвечься - часть2", url="https://vk.com/video-219877097_456239405")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
        [InlineKeyboardButton(text="Справочник по рыбам", url="https://ru.wikipedia.org/wiki/%D0%A0%D1%8B%D0%B1%D1%8B")]
    ]
)





