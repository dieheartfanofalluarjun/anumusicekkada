from pyrogram import Client
from Codexun.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from Codexun.config import (
    BOT_USERNAME,
    UPDATE, 
    SUPPORT, 
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,f"ʜᴇʏ 👋 ɪ ᴀᴍ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ, ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ᴀ ᴛɪᴍᴇ ᴛᴏ ᴛᴀʟᴋ ᴡɪᴛʜ ʏᴏᴜ 🙂 ᴋɪɴᴅʟʏ ᴊᴏɪɴ @{UPDATE} ғᴏʀ ɢᴇᴛᴛɪɴɢ sᴜᴘᴘᴏʀᴛ\n\nᴘᴏᴡᴇʀᴇᴅ ʙʏ @{SUPPORT}")
  return
