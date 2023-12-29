#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "26176218"
API_HASH = "4a50bc8acb0169930f5914eb88091736"
BOT_TOKEN = "6646145939:AAGN460KK9oTauwFC2cCTrYBzFnvIESu5cg"
SESSION = "BAGPatoAOj_nxBZo06MhTJMT0TrQAmN7_6shpq1nKbrf9iszrKTY6AXFwZ7Oy-47NEVMt2x93e7PXgHPCZKiI6Retmmi2VcHOSsmX5Z60lC3w3ZPtFYS10wKErbTy-rEiaiUIUhtvTg79xps0ZvGBEJk5rjgyu4hG3OPhQIwJCqKFJJRE7XFaZLzvoQ64oEgDNW-eN3nibsXAc7wItZEYRn1WmHwKn51TuaQ3ko6IJgvFtA0VAqeQGgWbtqB5zv6IT-gppOqF_S7S5OtaxyCT8_Zlg1OSF5pFECknYvW4BE2sARBR49EV9YndWLsKF9sX7UnWJl8mZSiyQEvDYm7abnCGhenCwAAAABBXjeKAA"
FORCESUB = "VZRENAMER"
AUTH = "1096693642"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = bot
bot.connect()
user=bot.get_entity('me')

Bot = bot

try:
    bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
