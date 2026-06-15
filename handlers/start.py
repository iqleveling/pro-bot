from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✏️ Rename", callback_data="rename"),
         InlineKeyboardButton("📄 Info", callback_data="info")]
    ])

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🚀 PRO BOT READY", reply_markup=menu())
