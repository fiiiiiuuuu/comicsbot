import os
import sys
from contextlib import suppress
from pathlib import Path

from dotenv import load_dotenv
from telegram import Bot

from download_comics import save_rand_comic


def send_photo(bot, chat_id, image_path: Path, caption: str):
    try:
        with image_path.open("rb") as f:
            bot.send_photo(chat_id=chat_id, photo=f, caption=caption)
    except FileNotFoundError:
        pass


def main():
    load_dotenv()
    bot = Bot(token=os.environ["TG_BOT_TOKEN"])
    caption, image_path = save_rand_comic()
    send_photo(bot, os.environ["TG_CHAT_ID"], image_path, caption)

    with suppress(FileNotFoundError):
            image_path.unlink()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
