import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from Codexun.utils.filters import command

from Codexun import BOT_NAME, BOT_USERNAME
from Codexun.config import BOT_USERNAME 
from Codexun.config import BOT_NAME
from Codexun.config import START_IMG

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**👋🏻 ʜᴇʟʟᴏ ᴡᴇʟᴄᴏᴍᴇ {message.from_user.mention()}**

💞 **ᴍʏ ɴᴀᴍᴇ ɪs**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Bot,** **ᴀ ʙᴏᴛ ғᴏʀ ᴘʟᴀʏɪɴɢ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴀɴᴅ ᴜɴʙʀᴇᴀᴋᴀʙʟᴇ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.*"

**ɴᴏᴡ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ɢᴜʏs [ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ](https://t.me/All_india_musicbot?startgroup=true) ᴡɪᴛʜᴏᴜᴛ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ ᴅᴇᴘʟᴏʏᴇᴅ ɪɴ ʜᴇʀᴏᴋᴜ sᴇʀᴠᴇʀ.**

**ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ 📚**""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📚ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmnds"), 
            ],[
            InlineKeyboardButton("✉️sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT}"), 
            InlineKeyboardButton("📡ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATE}"), 
            ],[
            InlineKeyboardButton("😏ʙᴀsɪᴄ ɢᴜɪᴅᴇ", callback_data="cbguide"), 
            InlineKeyboardButton("🙄ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="cbabout"),
            ],[
            InlineKeyboardButton("✚ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
