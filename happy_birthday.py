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




     
@Harsh.on(admin_cmd(outgoing=True, pattern="lovers (.*)"))
@Harsh.on(sudo_cmd(pattern="lovers (.*)(.*)", allow_sudo=True ))
async def furious(lovers):
    if lovers.fwd_from:
        return
    sed = lovers.pattern_match.group(1)
    made = lovers.pattern_match.group(2)

    
@Harsh.on(admin_cmd(pattern="hbd(.*)", outgoing=True))
@Harsh.on(sudo_cmd(pattern="hbd(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    words_interval = 1
    word_ttl = range(0, 36)
    birthday_boy = event.pattern_match.group(1)
    await event.edit("hbd")
    happy_birthday = [
        "HAPPY",
        "BIRTHDAY",
        f"{birthday_boy}",
        " May your birthday",
        "be the special day ",
        "that you receive",
        "all you ever desired.",
        f"HAPPY BIRTHDAY {birthday_boy} \n May your birthday be the special day \n that you receive all \n you ever desired  ",
    ]

    for i in word_ttl:

        await asyncio.sleep(words_interval)
        await event.edit(happy_birthday[i % 18])
        

CmdHelp("hbd").add_command(
  "f", "<name>", "Wishes Happy Birthday to the guy"
).add()
