#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = config("24454391", default=None, cast=int)
API_HASH = config("f1cc9ff726684360e45bdc612605f30b", default=None)
BOT_TOKEN = config("6733833024:AAGdWe34B21dZ9-hneLLnvQghBYTrgz1x9w", default=None)
SESSION = config("BQGqa00AMKuODo-WsqRXKtfzxdBOIsVb6PoROa5wseA-BXUAZfp34g3k_5-sDKvRc6H13FxscP0Z40eaL67dmWsLtc3O7er7A7GKnYaKS6X4hMS3nj5xmBXonn-QczabkbJ-vXfWPNiM2o1hEw5-rYM42EZE-svAXYDH0phQCzjhTPkej-AVwYQh0PufapbVEIAtkjXuxbJ6Q2OuFtb6np5MR2g0tKNKbo-z5fQJzSTXJ5LuN7bUUP3htVh_y3V29C0dtarpwlVnt54_-UVJKdiLHLU7lTRtr2XRJh5mrRoP30cYNk1zHkR4sWCWn45pI3JdjgeBPE0ZYTpAOWbYvw_B8SIEHwAAAAE9tQA7AA", default=None)
FORCESUB = config("official_satyam01", default=None)
AUTH = config("5330239547", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks.")
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
    # print(e)
    # logger.info(e)
    sys.exit(1)
