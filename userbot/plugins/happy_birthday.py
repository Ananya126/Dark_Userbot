# Coded by @Harsh-78 
# Kang with credits else gay

from os import name
from userbot.utils import admin_cmd ,sudo_cmd , edit_or_reply
from userbot import *
from userbot.utils import *
from userbot.utils import bot as Harsh
from telethon import events
import asyncio
from userbot.cmdhelp import CmdHelp




     

    
@Harsh.on(admin_cmd(pattern="hbd(.*)", outgoing=True))
@Harsh.on(sudo_cmd(pattern="hbd(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    words_interval = 1
    word_ttl = range(0, 8 )
    birthday_boy = event.pattern_match.group(1)
    await event.edit("hbd")
    happy_birthday = [
        "**HAPPY**",
        "**BIRTHDAY**",
        f"__{birthday_boy}__",
        "** May your birthday **",
        "**be the special day** ",
        "**that you receive**",
        "**all you ever desired.**",
        f" ** HAPPY BIRTHDAY __{birthday_boy}__ \n May your birthday be \n the special day \n that you receive all \n you ever desired. ** ",
    ]

    for i in word_ttl:

        await asyncio.sleep(words_interval)
        await event.edit(happy_birthday[i % 8])
        

CmdHelp("hbd").add_command(
  "f", "<name>", "Wishes Happy Birthday to the guy"
).add()





@Harsh.on(admin_cmd(pattern="shbd(.*)", outgoing=True))
@Harsh.on(sudo_cmd(pattern="shbd(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    words_interval = 5
    word_ttl = range(0, 6 )
    birthday_boy = event.pattern_match.group(1)
    await event.edit("shbd")
    happy_birthday = [
    
        "Kya be chutiye aaj birthday hai na tera ? ",
        "Birthday hai to khushi kyu mana raha hai chutiye ?",
        " Dharti par bojh hai tu chullu bhar paani me dub mar ",
        " wo chod tere liye special gift rakha hai maine shaam ko ghar aana mere aur apne liye painkiller bhi lete aana .",
        "Waise ye Sab chod  ",
        f"Happy Birthday{birthday_boy} lodu , Bhagwaan kare tu randwa naa rahe is saal.",
         ]

    for i in word_ttl:

        await asyncio.sleep(words_interval)
        await event.edit(happy_birthday[i % 6])
        

CmdHelp("Happy birthday").add_command(
  "hbd", "<name>", "Wishes Happy Birthday to the guy"
).add_command(
  "shbd", "<name>", "Wishes special Happy Birthday to the guy"
).add()





