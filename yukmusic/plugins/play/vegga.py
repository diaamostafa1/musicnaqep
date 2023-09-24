import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint

#▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▒▒▒▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▇▇▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▇▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▆▆▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▜▒▒▇▇▒▒▆▆▆▆▆▆▆▆▆
#▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▙▇▇▇▇▇▇▉▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▇
#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒KIᑎG ᗷᗩՏᕼᗩ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

                
@app.on_message(
    command(["مطورين افتار","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/74887c4af9749766c7333.jpg",
        caption=f"""**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين افتار ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ𓆩˹ ََ Տᗯᗩᗪ ،ِّّ⸙⛥َٰ ( ٍّސاމ)𓆪𓆃", url=f"https://t.me/DIV_MUHAMED"), 
                   ],
                   [                        
                    InlineKeyboardButton(
                        "ᯓ𓆩˹ ََ kᎥꪀᘜ᥆᥆ ،ِّّ⸙⛥َٰ 𓆪𓆃 ", url=f"https://t.me/TR_E2S_ON_MY_MOoN"),
                   ],
                   [                        
                    InlineKeyboardButton(
                        "★ᯓ𓆩˹ ََ ᥉𝗁Ꭵk᥆᥆ ،ِّّ⸙⛥َٰ 𓆪𓆃", url=f"https://t.me/SI_I_I"),
                ],[
                    InlineKeyboardButton(
                        "★ٍَ𑲭🇪🇬𑲭🇸🇦 𝙹𝙰𑲭 𝙲𝙺🇮🇶𑲭🇸🇾𑲭★", url=f"https://t.me/V_P_E"),
                ],[
                    InlineKeyboardButton(
                        "★𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⚡", url=f"https://t.me/source_av"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["روما","رولينا","حبيبت محمد","ست البنات","ملكه محمد"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("O_O_O_0_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷⌯𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍⌯⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
    
   



