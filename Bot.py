import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

WELCOME_TEMPLATE = """❅────✦ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 ✦────❅
SHADOW PHANTOM
User Info ⚡️
➻ NAME : {new_name}
➻ ID : {new_id}
➻ USERNAME : {new_username}
┯━━━━━▧▣▧━━━━━┯
•𝐆𝗿𝗼𝘂𝗽 •𝐑ᴜʟᴇꜱ•
⤷ 𝐍ᴏ 𝐏ʀᴏᴍᴏ
⤷ 𝐍ᴏ 18+ 𝐂ᴏɴᴛᴇɴᴛ
⤷ 𝐍ᴏ 𝐀ʙᴜsɪɴɢ 𝐒ᴘᴀᴍɪɴɢ
⤷ 𝐍ᴏ 𝐏ᴍ/𝐃ᴍ
┷━━━━━▧▣▧━━━━━┷
Any problem so tag {owner} or @admins
🔗 Join our Telegram channel:
✅ OWNER :- @BLACK_HAT_TEAM_1
"""

BUTTONS = [
    [InlineKeyboardButton("Instagram", url="https://www.instagram.com/naveen_anon_")],
    [InlineKeyboardButton("WhatsApp", url="https://wa.me/917840060614")],
    [InlineKeyboardButton("Channel", url="https://t.me/BLACK_HAT_TEAM_1")],
]

def welcome(update: Update, context: CallbackContext):
    for new_user in update.message.new_chat_members:
        text = WELCOME_TEMPLATE.format(
            new_name=new_user.full_name,
            new_id=new_user.id,
            new_username=new_user.username or "—",
            owner="@BLACK_HAT_TEAM_1"
        )
        update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(BUTTONS))

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
