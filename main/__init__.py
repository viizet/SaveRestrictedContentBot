#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "1144902"
API_HASH = "e743e5a4f35076e4c558a4bd713082e9"
BOT_TOKEN = "5744410448:AAGhJMwh_5N1UIqy-VF8FhyjJbQfeC_t2vg"
SESSION = "BQA5FO0UFgRwmLnT1Z7Umo_cLk-lwyCR8bjkJMN9JBp-9h6PVpyf4MGtvNb-Z0hYPi_zfmemhXtnSEhsCJxsCrgscNRTPWFdJTN5fvPcu3Z8fi_UCrCqL_gK8jE8dFGLmNEROP1DLGd23E48MgEJCDfOG5HDZtioIYcj3IoB3_kR3i37Fn0rDQ_ylAkYJLOJKrmvLqwL8p2IgakPl9k7vvx5IcNUEOOwc1tT_LfCp-fGL8aSeDo0fdl0HThXpISRsfE5Tj7TukwI7YBZNeKsrz71XX4YwEJ_v5WYqom6Hxu7f08MC1SKHkJ5Jugsz46wCsA22zSHQrFRnNGDvrEeTx73LPiwRAA"
FORCESUB = "hxbots"
AUTH = "754495556"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = bot

Bot = bot

try:
    bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
