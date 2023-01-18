#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "924859"
API_HASH = "a4c9a18cf4d8cb24062ff6916597f832"
BOT_TOKEN = "5744410448:AAGhJMwh_5N1UIqy-VF8FhyjJbQfeC_t2vg"
SESSION = "1BVtsOIEBu16K4mvZ_QE4uAFUHt0GNtqCWaZTZLDF71mARKqFEVuW9fOuMpkBIKK4DHI0hMsaKulEWrgYyHh5QcH8iflzjN3UxqWw6fQxn4OPHOQkJTz_7-4IP_xipqhmiP1Twr5PbEiJ8O3TwouHt9PBa5A2jyINyfshqhyuGdGaGdVZjGuP-8exladQXLzQMDR3ktpba9el5HJKdBMCzB_xoU5IxOY9huY1zd7bKgqdGtzhBOn3vEEUkRiY_iZBCPczOuLDD1w2JUDPedmFG1IrA9Qk3gCnOwDNZLxChWOcK1gmx6WXb9fW8AB1wnFu4sx7yHPXfX4O29c_lawJI-snPxiJNCQ="
FORCESUB = "hxbots"
AUTH = "754495556"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = bot
phonenum = '+918742089059'
bot.connect()
user=bot.get_entity('me')

Bot = bot

try:
    bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
