import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.markdown import hbold
from config import Token
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

TOKEN = Token

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("image"))
async def sen_photo(message: types.Message):
    file_ids = []

    with open("qr.webp", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="qr.webp"
            ))

        file_ids.append(result.photo[-1].file_id)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
