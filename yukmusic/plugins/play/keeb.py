import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from YukkiMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.regex("^$"))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**اهلين {user} !\n- اضغط الزر عشان تشوف اوامر البوت**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^ما الاائيات$") & filters.user(208912006))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"**✧ اهلين مطوري ارحب\n- هذي احصائيات ميرا ياعيني :\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾**")
    await m_reply_text("")


@app.on_message(filters.command("","."))
def vgdg(client,message):
        message.reply_text(
            f"""✧ Welcome Baby,
ᴅᴇᴠᴇʟᴏᴘᴇʀ -› [SeMo ♪](t.me/S_E_M_O_E_L_K_B_E_R)
ᴄʜᴀɴɴᴇʟ -› [ElNgOom](t.me/SOURCE_ELNGOM)""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ChNnEl SoUrCe ♡", url=f"t.me/SOURCE_ELNGOM")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("مي ناطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001580518434, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشات تشوف التحديثات** -› [• Source Mira •](t.me/SOURCE_ELNGOM)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "- اهلا يبرو تحكم من الازرار اسف"




REPLY_MESSAGE_BUTTONS = [

         [

             ("كيفية استخدام البوت"),                   

             ("اوامر البوت")




          ],

          [

             ("المطور"),

             ("SOURCE")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^SOURCE$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب النجوم**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("كيفية استخدام البوت"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت اتبع الخطوات الي بالاسفل**
1 • ارفع البوت مشرف
2 • سيتم التشغيل تلقائي 
- لو واجهت مشكله كلم مطور البوت ~ @S_E_M_O_E_L_K_B_E_R""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "SeMo", user_id=5183920797),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلا بيك حبيبي لو عجبك السورس وعاوز تنصب بوت التواصل اسفل **
مطور السورس -› [SeMo](t.me/S_E_M_O_E_L_K_B_E_R)
قناة السورس -› [𝑠𝑜𝑢𝑟𝑐𝑒 𝑒𝑙𝑛𝑔𝑜𝑜𝑚](t.me/SOURCE_ELNGOM)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ChNnEl SoUrCe ♡", url=f"https://t.me/SOURCE_ELNGOM"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = "- هلا فيك في قسم اوامر البوت"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("طريقة ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.group & command("اوامر البوت"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.group & command(""))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.group & command("شرح التشغيل بمنصات الاغاني"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓
• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify
[𝑠𝑜𝑢𝑟𝑐𝑒 𝑒𝑙𝑛𝑔𝑜𝑜𝑚](t.me/SOURCE_ELNGOM)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("اوامر المجموعة"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""اوامر التشغيل في المجموعه\nتشغيل + اسم الاغنيه للايقاف -اسكت او ايقاف -تخطي """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.group & command("اوامر القنوات"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""اهلا عزيزي اوامر القنوات مثلا تشغيل واسم الاغنيه وللتحكم ازازر اسفل كليشه التشغيل 💕""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & command("طريقة التنزيل"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلا في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓
[ تتزيل + اسم المطلوب ..]
مثال -› تنزيل بحبك وحشتني
- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("حفظ التشغيل"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & command("طريقة ربط القنوات"))
async def dowhmo(client: Client, message: Message):
        await message.reply_text("""اهلا عزيزي التشغيل في القنوات مباشر مثل الجروب تشغيل + اسم الاغنيه**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيف البوت لمجموعتك", url=f"https://t.me/{app.username}?startgroup=True"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
