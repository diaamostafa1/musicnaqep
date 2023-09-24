import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import *
from YukkiMusic import app


@app.on_message(filters.voice_chat_started)
async def brah(client, message):
       await message.reply("تم بدا محادثة صواتية جديدة.")
       
@app.on_message(filters.voice_chat_ended)
async def brah2(client, message):
       await message.reply("تم انهاء المحادثه الصواتيه.")
       
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client, message):
           text = f"قام : {message.from_user.mention}\nبدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"{user.mention} "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} .")
           except:
             pass