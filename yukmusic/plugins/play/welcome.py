import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from YukkiMusic import app
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters

@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"-نورتتنا ي برو : ✨ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
	
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"-شرفتنا الشوايه دول ولله سلام : ✨ʏ  {message.from_user.mention} ",chat_id=chatid)
	
	
	
	
	
	
	
@app.on_message(
    command(["سيمو","المبرمج", "صاحب السورس"])
    & filters.group
  
)
async def kkpp(client, message):
    usr = await client.get_chat("S_E_M_O_E_L_K_B_E_R")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**DevElPor sOuRcE ElNgOoM : ✨\n\n🥷: NaMe  :{name}\n🦸: UsEr :@{usr.username}\n🗽: Id :`{usr.id}`\n✨: BiO :{usr.bio}\n\n**لو محتاج حاجه يبرو تواصل معايا خاص : ✨**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
