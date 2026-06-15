from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "pro_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=100,
    max_concurrent_transmissions=20
)

import handlers.start
import handlers.rename
import handlers.info

app.run()
