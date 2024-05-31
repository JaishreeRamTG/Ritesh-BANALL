import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))  # Convert to list of ints
OWNER = "I_RITESH_I"
# Pyrogram client
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

def is_sudo_user(user_id):
    return user_id in SUDO_USERS

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    if not is_sudo_user(message.from_user.id):
        return
    await message.reply_photo(
        photo="https://telegra.ph/file/fff2ee6f504bc061cb7d3.jpg",
        caption=("ʜᴇʏ, ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ "
                 "ʟɪʙʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜɪɴ "
                 "ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs!\n\nᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪʙ me ғᴜʟʟ ᴘᴏᴡᴇʀs\n\nᴛʏᴘᴇ /ʙᴀɴᴀʟʟ "
                 "ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ."),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER}")]]
        )
    )

@app.on_message(filters.command("b") & filters.group)
async def banall_command(client, message: Message):
    if not is_sudo_user(message.from_user.id):
        return
    print("Getting members from {}".format(message.chat.id))
    async for member in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
            print("Kicked {} from {}".format(member.user.id, message.chat.id))
        except Exception as e:
            print("Failed to kick {} due to {}".format(member.user.id, e))
    print("Process completed")

# Start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
