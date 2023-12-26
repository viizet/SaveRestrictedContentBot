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
BOT_TOKEN = "6720741095:AAFRnLXaHMuF00S9r_EbI4O63Z5sQYAK6W0"
SESSION = "BAE2OXsAtwrqNWV7EmeO4zL8qHPvWAn6CDb1In2GcLfkNHNppMVpEank7SWP-iJnZkrh3EBennytFzJGwnX371kJOdpQNR1dl645VlhLCJ0KffejETSnr9HPHnhTlLr4559BK6Fp0yrcUPxk-dgtUXlkfzIhWrjP3gKlbCFbXURN0yjFPnfQjx_aWGe2f1dOLchQ4bvnf4Pb3FfPQmUsfk94lWiKDWH1kZOfyeeV13gofghq6_0010_9lSv53uAfBg7hIVlMkP0JbUIbcpVI3CzGdkKzjCS8LIi-6QVlkimxNCsRpqJnzmktbv8QEBDZ5wB1uGBrRkd9HHMMGiQobif9WxXUaQAAAAFTD5D8AA"
FORCESUB = "VzSaverestrictedcontent"
AUTH = "1096693642"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = bot
phonenum = '+256704101759'
bot.connect()
user=bot.get_entity('me')

Bot = bot

try:
    bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
