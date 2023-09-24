import asyncio
from pyrogram import Client, filters
from YukkiMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

iddof = []
@app.on_message(
    command(["قفل الايدي","تعطيل الايدي"])
    & filters.group
  
)
async def iddlock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("الامر معطل من قبل عزيزي 🚦")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي عزيزي : 🦸")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")

@app.on_message(
    command(["فتح الايدي","تفعيل الايدي"])
    & filters.group
  
)
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل عزيزي  : 🥷")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم  تفعيل الايدي عزيزي : 🦸")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")




@app.on_message(
    command(["ايدي","الايدي","ا"])
    & filters.group
  
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""🦸 : NaMe :{message.from_user.mention}\n🗽 : UsEr :@{message.from_user.username}\n🚦 : Id :`{message.from_user.id}`\n🥷 : BiO :{usr.bio}\n⚡ : ChAT: {message.chat.title}\n🌐 : Id ChAt :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(
    command(["قفل جمالي","تعطيل جمالي"])
    & filters.group
  
)
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي معطله بي الفعل : 🥷")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح : 🚦")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")

@app.on_message(
    command(["فتح جمالي","تفعيل جمالي"])
    & filters.group
  
)
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("جمالي مفعله من قبل : 🌐")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم قفل جمالي بنجاح : 🗽")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")




@app.on_message(
    command(["جمالي"])
    & filters.group
  
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       

