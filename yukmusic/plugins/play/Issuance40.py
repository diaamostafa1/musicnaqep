import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار","حول"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/825fc701fb4794c483ce5.jpg",
        caption=f"""**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-أفـاتـار
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-يوكي بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-10-4-2022
★᚜ مـأسسـيـن  أفـاتـار:- [⎖᳒𝙈𝙊𝙃𝘼𝙈𝙀𝘿⌯⤹𝐊𝐈𝐍𝐆⤸](https://t.me/U_UU_O)

**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⊷𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⊶★", url=f"https://t.me/source_av"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


