from pyrogram import Client, filters
from pymediainfo import MediaInfo

# When user clicks Info
@Client.on_callback_query()
async def info_btn(client, query):
    if query.data == "info":
        await query.message.reply("📤 Send file to get full info")

# When user sends file
@Client.on_message(filters.document | filters.video)
async def get_info(client, message):
    file = await message.download()

    media_info = MediaInfo.parse(file)

    audio_tracks = 0
    subtitle_tracks = 0

    for track in media_info.tracks:
        if track.track_type == "Audio":
            audio_tracks += 1
        elif track.track_type == "Text":
            subtitle_tracks += 1

    await message.reply(
        f"🎬 FILE INFORMATION\n\n"
        f"🔊 Audio Tracks: {audio_tracks}\n"
        f"💬 Subtitles: {subtitle_tracks}"
    )
