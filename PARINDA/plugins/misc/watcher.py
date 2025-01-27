from pyrogram import filters
from pyrogram.types import Message

from PARINDA import app
from PARINDA.core.call import parinda

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await parinda.stop_stream_force(message.chat.id)
