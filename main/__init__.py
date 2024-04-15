#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 18717081
API_HASH = "cbafb107aea26ae983f0924b4739a20e"
BOT_TOKEN = "7064787118:AAFTVpfvGzq7OmTAijttZ8ESFMcKCqioZys"
SESSION = "BQEdmZkAwCri8oTC9a8lxc1kePR_iHKyJP7tbPIBmMjqz3E6NsD2K5cRjdgkC_fNugg-U99fAIJWVU2pndHU0RsDZo35g0xzgLwQakA8aELO5uRz6Z2IOhVkQLehX_RLhDGTK7n8APsKrtyaWXCMd5KP002a96LxHo5eoJRUyewQqfS6x-SHOPlXt_DYVSBm4CKlx5gmu6IxFUDJ65Dp2QHGE55iRs1cqfQNfXZ27eJvjDLtUexx3FeSpa-ZT_cC39_Avn0tQIDav6xq7h-F2Xjt_rOfuAAJySSwsVLKvkjQ2hATBW5pXhtOE3e7KI_2RET2RAC0yNx_41i0VqV342wznrfnqQAAAAFF4RiQAA"
FORCESUB = "fmwlproof"
AUTH = 5467347088

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
