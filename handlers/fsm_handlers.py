from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import F
from database import add_user
from aiogram.fsm.context import FSMContext


class Form(StatesGroup):
    name = State()
    love_fishes = State()

fsm_router = Router()

@fsm_router.message(Command("form"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет рыбак. Как тебя звать?")
    await state.set_state(Form.name)

@fsm_router.message (Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("а тебе нравиться ловить рыбу")
    await state.set_state(Form.love_fishes)


@fsm_router.message(Form.love_fishes, F.text.casefold() == "yes")
async def process_like_write_fishes(message: Message, state: FSMContext) -> None:
    await state.update_data(like_fishes="yes")
    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        name=data['name'],
        like_fishes=data['like_fishes']
    )
    await state.clear()
    await message.reply(
        text="o kak",
        reply_markup=ReplyKeyboardRemove()
    )