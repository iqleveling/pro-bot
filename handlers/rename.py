from pyrogram import Client, filters
from database import get_user
import os

# Button click
@Client.on_callback_query()
async def rename_btn(client, query):
    user = get_user(query.message.chat.id)

    if query.data == "rename":
        user["mode"] = "rename"
        user["queue"] = []
        await query.message.reply("📤 Send files to rename")

# Receive files
@Client.on_message(filters.document | filters.video | filters.audio)
async def file_handler(client, message):
    user = get_user(message.chat.id)

    if user["mode"] == "rename":
        path = await message.download()
        user["queue"].append(path)

        await message.reply(f"✅ File added: {len(user['queue'])}")

# Process rename
@Client.on_message(filters.text)
async def process(client, message):
    user = get_user(message.chat.id)

    if user["queue"]:
        base = message.text
        count = 1

        await message.reply("🚀 Renaming started...")

        for file in user["queue"]:
            ext = os.path.splitext(file)[1]
            new_name = f"{base}_{count}{ext}"

            os.rename(file, new_name)

            await message.reply_document(new_name)

            os.remove(new_name)
            count += 1

        user["queue"] = []
        await message.reply("✅ All files renamed successfully!")
