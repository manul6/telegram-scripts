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
import json

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN', 'your_bot_token_here')
SOURCE_TO_TARGETS_FILE = os.getenv('SOURCE_TO_TARGETS_FILE')
SOURCE_TO_TARGETS = None

with open(SOURCE_TO_TARGETS_FILE) as input_mapping:
    SOURCE_TO_TARGETS = json.load(input_mapping)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.channel_post()
async def forward_post(message: types.Message):
    for forward in SOURCE_TO_TARGETS:
        if message.chat.id == forward["from"]:
            for to in forward["to"]:
                await message.forward(to)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
