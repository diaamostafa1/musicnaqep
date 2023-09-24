import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["مصنع","المصنع","مصنع أفـاتـار"])
    & filters.group
    
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/825fc701fb4794c483ce5.jpg",
        caption=f"""[⭑ٖٖꪝᥱᥣᥴ᥆꧑ᥱ ƚ᥆ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ᥉ᥱᥴƚᎥ᥆ꪀ᥉ ☽](https://t.me/source_av) 

★ هاا هالو عزيزي : \n│ \n└ʙʏ: {message.from_user.mention()}**
★ اختار ما تشاء من أقسام أفـاتـار المختلفه
★ من مصانع..أفـاتـار مختلفه..و بمميزاتها""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹⩹★⊷𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⊶★⩺️", url=f"https://t.me/source_av"),
                   ],
                   [
                    InlineKeyboardButton(
                       "◉ ᴀᴠ 𖣂 ᴘʀᴏᴛᴇᴄᴛɪᴏɴ", url=f"https://t.me/AV_MA_BOT"),
                   ],
                   [
                   InlineKeyboardButton(
                        "◉ ᴀᴠ ᴍᴜѕɪᴄ𖣂ᴍᴀᴋᴇʀ", url=f"https://t.me/Avmusicmaker"),
                   ],
                   [     
                    InlineKeyboardButton(
                        "◉ ᥲ️᥎ ƚᥱᥣᥱƚᏂ᥆ꪀ ", url=f"https://t.me/A_O_Il"),    
                   InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
        ),
    )