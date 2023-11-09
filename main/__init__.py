#Github.com/Vasusen-code

from pyrogram import Client
import os

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from .decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN","")
#Mine Pyrogram
SESSION = str(os.environ.get("SESSION","BQGfIaIAWgQ1tXZNPlGeCigVu1-ygmVOacm2xzolDcS6S1FbbnWLM-k3B7JKOPuJI5Nq6AsP1dwq37Uid6Ktf1tkS2NiTXFZX113PN8K8HawIDLsOLlkrZV9HEiLaC8b2gk3Zzl1d7aSLR0iU0_zL977lt2WeibYBHvI7MscMFCELoVdbliJ5QY4J_qxkzefHBItzCWnxplpzbjCy9H2TegGq6cuFwb4NbJAvRrcrd1x1Oa-DEfuN80PhfrxB88R_kOKgwd0NY31FS1iwHY1VnopnsFNZ6mUEQ4TQWJNLIZjHzT7wyOBx15wCow9q7PGXagsYXDP8iPEr1Ix7mppZDXnABchQQAAAAFDitGHAA"))

AUTH = int(os.environ.get("BOT_OWNER", "746480452"))
FORCESUB = config("FORCESUB", "Joint0T")



bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    name="Your_bot_name",
    session_string=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "Your Bot Name",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
