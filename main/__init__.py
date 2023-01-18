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
SESSION = "BQBc-T2lOk0U45xTQjGR8CKLqCxQoy5EWgjSm_9gppzbxao0cgTSip9iUYi4P5qn04Jobfz67y7PISmS2MZDJgmhBfciH8HpI_V5AelnTz4CXYQBIElolU5vdI9efaqnyC-hPFdCv7_FDDF8lFSJ4K2_S5eYDnzh_2ghPmFP8MjdPKM4FLB5yfVk0m_rMIFEhiCoE2CclTT0Od7q00fIyyBDkmJ_PZsnc8ZfdJY0eF5yspnZX93tYStd6lXg40YqqMdfSibH-LKfgZ5byos5YKA43KinqsPuGx42zOImCtcHjac1liIJH9Gvq9yT17_XqXkKgOOdufEsrik7yvwcPP0ZLPiwRAA"
FORCESUB = "hxbots"
AUTH = "754495556"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
