import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس سيمو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/WORLED_SEMO/338",
        caption=f"""**╭── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/SOURCE_ELNGOM) • ──╮**

**[⌯𝗗𝗘𝗩: 𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/S_E_M_O_E_L_K_B_E_R)**

**[⌯𝗦𝗨𝗣𝗣𝗨𝗥𝗧: 𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/T_S_T1)**

**[⌯𝗖𝗛𝗔𝗡𝗡𝗘𝗟: 𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/SOURCE_ELNGOM)**

**[⌯𝗠𝗔𝗞𝗘𝗥: 𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/ELNGOOMM_BOT)**

**╰── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/SOURCE_ELNGOM) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "HeLp GrUoB.", url=f"https://t.me/T_S_T1"), 
                ],[
                    InlineKeyboardButton(
                        "𝗗𝗘𝗩 𝗦𝗘𝗠𝗢 ◍", url=f"https://t.me/S_E_M_O_E_L_K_B_E_R"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك ◍", url=f"https://t.me/SPPED_MUISC_BOT?startgroup=true"),
                ],

            ]

        ),

    )
    
    