#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27171299
API_HASH = "a0a498768344084b93579cfbdddf6f08"
BOT_TOKEN = "5690273417:AAEACpMgmHhiylx0qnRepERdFsqa6kFU1CY"
SESSION = "BQDC6iGma753jGHiUmGPFx84Lq6yIIkSNBPJAOT97RoEfihCSPYrLYQgtHPGCcP35SdfUz_UGXG7aNCP2cTuB3G9Zht4d25CYDiqCBgSkENoihe1PUjuwcYav8mCXOhtHlwPk9sX-CixJZjIjM5wSHlOXu2fK1k6_I1cG7E9zXQ781j4Zi1ai0LjwXGeWlvBa2hMF15jWkohdgMR7uDhhTV6j0x02Z1BldJs9rSDx1YCKwrgZ5BXXPNJTyYNs317JmecbsR2SDAWPutL7mZgDBpkWQ5bUyEOyTOwPwQD6FO580pmtFxwnTktQL3XjJABsz2pEm8_lwoVIO1RrdP7DH22AAAAAWPKvEkA"
FORCESUB = "Arshad_Tech"
AUTH = 5969198153
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
