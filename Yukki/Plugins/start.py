import yt_dlp
from pyrogram import filters
from pyrogram import Client
from youtubesearchpython import VideosSearch
from Yukki import app, SUDOERS, BOT_ID, BOT_USERNAME, OWNER
from Yukki import dbb, app, BOT_USERNAME, BOT_ID, ASSID, ASSNAME, ASSUSERNAME
from ..YukkiUtilities.helpers.inline import start_keyboard, personal_markup
from ..YukkiUtilities.helpers.thumbnails import down_thumb
from ..YukkiUtilities.helpers.ytdl import ytdl_opts 
from ..YukkiUtilities.helpers.filters import command
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Yukki.YukkiUtilities.database.chats import (get_served_chats, is_served_chat, add_served_chat, get_served_chats)
from Yukki.YukkiUtilities.database.queue import (is_active_chat, add_active_chat, remove_active_chat, music_on, is_music_playing, music_off)
from Yukki.YukkiUtilities.database.sudo import (get_sudoers, get_sudoers, remove_sudo)

def start_pannel():  
    buttons  = [
            [
                InlineKeyboardButton(text="📚 Commands", url="https://telegra.ph/Vayu-Music-03-11-2")
            ],
            [ 
                InlineKeyboardButton(text="📣 Channel", url="https://t.me/RidhamChannal"),
                InlineKeyboardButton(text="💭 Group", url="https://t.me/RidhamMusicc")
            ],
    ]
    return "✨ This is Ridham music, a bot that can play music trought the Telegram Group video chat.", buttons

pstart_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to a Group ➕", url="http://t.me/RidhamMusic_Bot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "♥️ 𝗢𝘄𝗻𝗲𝗿 ", url="https://t.me/vayu60"),
                    InlineKeyboardButton(
                        "❤️ Aditi Id ", url="https://t.me/Aditidillon")
                ],[
                    InlineKeyboardButton(
                        "👥 Ridham Group", url="https://t.me/RidhamMusicc"), 
                    InlineKeyboardButton(
                        "📣  Ridham Channel", url="https://t.me/RidhamChannal")
                ],[
                    InlineKeyboardButton(
                        "❓ First read guide", url="https://telegra.ph/Vayu-music-Guide-03-11-2"),
                    InlineKeyboardButton(
                        "📚 Commands", url="https://telegra.ph/Vayu-Music-03-11-2")
                ]
            ]
        )

welcome_captcha_group = 2
@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
       await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(f"🧙🏻‍♂️ • {member.mention} •\n\n• **Staff** of 𝓡𝓲𝓭𝓱𝓪𝓶 𝓶𝓾𝓼𝓲𝓬𝓬 has joined this Group.")
            if member.id in SUDOERS:
                return await message.reply_text(f"🧙🏻‍♂️ • {member.mention} •\n\n• **Staff** of 𝓡𝓲𝓭𝓱𝓪𝓶 𝓶𝓾𝓼𝓲𝓬𝓬 has joined this Group.")
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(f"❤️ **Thanks for adding me to the group !**\n\n**Promote me as administrator of the group, otherwise I will not be able to work properly.", reply_markup=InlineKeyboardMarkup(out[1]))
                return
        except:
            return

@Client.on_message(filters.group & filters.command(["start", "help"]))
async def start(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
       await add_served_chat(chat_id)
    out = start_pannel()
    await message.reply_text(f"✨ Hello {message.from_user.mention}, i'm 𝓡𝓲𝓭𝓱𝓪𝓶 𝓶𝓾𝓼𝓲𝓬𝓬.\n\n💭 Appoint me as admin in your Group so i can play music, otherwise you can't use my service.", reply_markup=InlineKeyboardMarkup(out[1]))
    return


@Client.on_message(filters.private & filters.incoming & filters.command("vplay"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "["+user_name+"](tg://user?id="+str(user_id)+")" 
        await app.send_message(message.chat.id,
            text=f"✨ Welcome {rpk} !\n\n💭 [ 𝓡𝓲𝓭𝓱𝓪𝓶 𝓶𝓾𝓼𝓲𝓬𝓬 ](https://t.me/RidhamMusic_Bot) **Can** play music on your **Groups** through the **Telegram Group call** feature !\n\n💡 **Check out** all the **Bot's commands** and how they work by clicking on the » ✅ **Commands** button!",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
            disable_web_page_preview=True
        )
    elif len(message.command) == 2:
        chat_id = message.chat.id                                                       
        query = message.text.split(None, 1)[1]
        f1 = (query[0])
        f2 = (query[1])
        f3 = (query[2])
        finxx = (f"{f1}{f2}{f3}")
        if str(finxx) == "inf":
            boom = await app.send_message(chat_id, "🔍 Getting info...")
            query = ((str(query)).replace("info_","", 1))
            query = (f"https://www.youtube.com/watch?v={query}")
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channel = result["channel"]["name"]
                link = result["link"]
            searched_text = f"""
💡 **Track Informations**

🏷 **Name:** {title}
⏱ **Duration:** {duration}
👀 **Views:** {views}
📣 **Channel:** {channel}
🔗 **Link:** {link}

⚡️ __Powered by Vayu music AI__"""
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await boom.delete()
            await app.send_photo(message.chat.id,
                photo=thumb,                 
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "🧙🏻‍♂️ **List of sudo users:**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:                     
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue                     
                text += f"➤ {user}\n"
            if not text:
                await message.reply_text("❌ no sudo users found")  
            else:
                await message.reply_text(text)
