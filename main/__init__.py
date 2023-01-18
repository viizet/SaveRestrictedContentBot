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
SESSION = "1BVtsOKkBu3Mkg69EJGWgLtAR-E3eL7aNrogmsxYQj9JOqe0AaivzMiB_xrOVgWvZEx-iriuQaDRexXNhQPO3KPtKG4BdxZ6wMUOkgYAZlI5sCfIFK3yOxNrwU-AFWVZesOLDZCn61mmAe71bcQSQ--l5sqbclVIvrFVOaOxcoupda59lBSTK-lJfZPBFGMRWVW22TyD_zmmbTA2wJQWwmUTHBAQLhqISCHjFRL5x-MWF7Ybv6EcpZwy93yLFMSg5wD3IVs4hSzrhHV4Av1K4eMxV87U5Rkagm-nMlZIT93w446Y_wAp3FVVHHz6h_94rvL2cfsa2Q9VDCCW6Qy1b2J0G9hkF8AU="
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
