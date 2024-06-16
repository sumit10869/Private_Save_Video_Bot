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
SESSION = config("BQGqa00AKpOaDAdVn7eghXguqzPskn0nFz-yZKWFwdnG0EGsitCYKujnigc3-Q0J5FMvvQE5WJYHiYzUIo71Pm_71yNrxF5AbJNdM0GS5GkGFa3wMgkdMiDkLeaxhDLCayXAVmZz9bWHKvx60KFOHTFcVEVhJhB0Pm1fZOoFwHveWJYilK4aBvX3-g8XJydpEw4iCFhBqSM1k1awCupZGEZQTRGHon5xsn9AQJ6Qhoun21LdvS0-mY_QrNLVg1zmLn5PxTY5O9_Kab-a_iOmNnQUysOF4qqhqxHp8YgL7bVu9EZOLENZcDuI3ro4lfToPCG6WPJ2aHCDTMl39OQlj-p6DSNWEgAAAAFrC_JdAA", default=None)
FORCESUB = config("official_satyam01", default=None)
AUTH = config("6090912349", default=None)
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
