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
BOT_TOKEN = "1779838194:AAG6wRcF4mml3r0ZAD1Txy2fehxoS5QJRD4"
SESSION = "BQBdNU7gqnSDCqnUDQftXhc51QiUmGpk0fCmLRTM6M9sVCYL9aCvEDSPJYwdsh5q0OG-GznglgP-lmlWsUDdtsXjbEalL3IaSyA4UPmbDFsAOwwFXPITPiVAoDoPnNwqlgkN00PO0Y2VWjJT5pQ_F8c2KW9E_uF8ikcKVgXMiHkARS2NBXKuJg09sHKf46oUgaL2Nt98THeX-pF9E9P9Xlki1sxlAPK0Bo9BUBaVLimUCNsRnd4cRZRoHbBudOqRHv9As5I36mx1WrdEW5L5fI_w7qViPm_SkHjP5Lp6XV5t3DCOA42-cuO21jnUvm_kZSc92bQ3ZnU9tecIHYRYlM4PLPiwRAA"
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
