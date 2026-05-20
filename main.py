import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

TOKEN = "ТВОЙ_ТОКЕН"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Привет! Бот работает!"
    )

@dp.message()
async def echo(message: Message):
    await message.answer(
        f"Ты написал:\n{message.text}"
    )

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
