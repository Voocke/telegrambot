import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from random import randint


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6877459397:AAFHxn7WXz_TRzLJQ89n_hweoTXsdgsXTeU")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
        types.KeyboardButton(text="Бриф"),
        types.KeyboardButton(text="Контакты"),
        types.KeyboardButton(text="/Меню")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите ответ")
    await message.answer("Привет! Я - БРИФБОТ, и я помогу тебе сделать твой заказ быстро и точно", reply_markup=keyboard)


@dp.message(Command("Меню"))
async def cmd_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
  
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(Command("main"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())