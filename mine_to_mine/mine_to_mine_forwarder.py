#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "aiogram",
#     "dotenv"
# ]
# ///

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

import asyncio
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN', 'your_bot_token_here')
SOURCE_CHANNEL_ID = int(os.getenv('SOURCE_CHANNEL_ID', '-1001234567890'))
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID', '-1009876543210'))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.channel_post()
async def forward_post(message: types.Message):
    if message.chat.id == SOURCE_CHANNEL_ID:
        await bot.forward_message(
            chat_id=TARGET_CHANNEL_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
