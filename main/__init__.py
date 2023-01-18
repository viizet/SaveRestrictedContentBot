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
SESSION = "1BVtsOKkBu1FR7ZXDc6JRVaHMv-XQb56rKC_PiGvf895XknubTkvm4gnMCvZHdv2UAIzQTFklxDuaBwP3F-ZOZ2YcyrbAGEtw-yrmBqZq6rxbgfpCeh7MimqZWUjfU091wcMov2YLkdmEVKJ9_mm73KCIxFBxz56InKpP2VuZ8u5LuIib6iJfXuClOsziHm30nwjf_co4TK6Rp2YT7Kd4Y3brrTdM7b9WZFkDrhX_79fiTi61x_Vcev5AidosoHslLYvMZ06yGsqgpw2hg-wjRwPiApCp2F9VBsP89cjiKauwXmBNCxrYklNlck0uM2_JZRV-AX5_luMxfpG_-vkxFM0GS3SuqvY="
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
