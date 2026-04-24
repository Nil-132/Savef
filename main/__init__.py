# Github.com/Vasusen-code

from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# -------------------- Load environment variables --------------------
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

# --------------------------------------------------------------------
# CLIENT CREATION ONLY – NO .start() CALLS HERE
# --------------------------------------------------------------------

# Telethon bot client (used for bot methods)
bot = TelegramClient('bot', API_ID, API_HASH)
# Note: .start(bot_token=...) will be called in main/__main__.py

# Pyrogram userbot (string session)
userbot = Client(
    "saverestricted",
    session_string=SESSION,
    api_hash=API_HASH,
    api_id=API_ID
)

# Pyrogram bot client
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)
