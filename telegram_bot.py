import dotenv
import os
from telegram import Bot
import asyncio
from main import main

async def send_photo(bot, chat_id):
    comic_caption, filename = main()

    with open(filename, 'rb') as f:
        await bot.send_photo(chat_id=chat_id, photo=f, caption=comic_caption)

    os.remove(filename)
        

async def run_bot():
    dotenv.load_dotenv('.env')
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    bot = Bot(token=tg_bot_token)
    chat_id = tg_chat_id

    await send_photo(bot, chat_id)

if __name__ == '__main__':
    asyncio.run(run_bot())