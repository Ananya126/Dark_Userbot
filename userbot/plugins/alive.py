
from userbot import *

from userbot.utils import *

from telethon.events import NewMessage

from telethon.tl.custom import Dialog

from telethon.tl.types import Channel, Chat, User





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Darkbot User"



ludosudo = Config.SUDO_USERS

if ludosudo:



    sudou = "True"



else:

    sudou = "False"

    

dark = bot.uid



PM_IMG = "https://telegra.ph/file/bd05af18c9b4fc5b57233.mp4"



pm_caption = "__**🤘『 ÐΛR̷Ꮶ 』★BØT★ ɨz օռʟɨռɛ🤘**__\n\n"



pm_caption += (

    f"           𖤍M͜͡Y͜͡ B͜͡O͜͡S͜͡S͡𖤍\n**『🔥[{DEFAULTUSER}](tg://user?id={dark})🔥』**\n\n"

)







pm_caption += f"🔥**『 ÐΛR̷Ꮶ 』★BØT★🔥  : 1.0** \n\n"



pm_caption += f" ** ⚔️𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ 𝕍𝔼ℝ𝕊𝕀𝕆ℕ ⚔️  : 6.9.0 ** \n\n"







pm_caption += "**⭐𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕊𝕋𝔸𝕋𝕌𝕊⭐ :- 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕎𝕆ℝ𝕂𝕀ℕ𝔾 ℕ𝕆ℝ𝕄𝔸𝕃𝕃𝕐 **✅\n\n◆"





pm_caption +=  "**⭕ℂℍ𝔸ℕℕ𝔼𝕃⭕    : [ᴊᴏɪɴ](https://t.me/Dark_bot_support)**\n\n" 







pm_caption += "**⭐ℂℝ𝔼𝔸𝕋𝕆ℝ ⭐: [ ʜᴀʀsʜ ʜᴇʀᴇ](https://t.me/harsh_78)**\n\n"



pm_caption +=  "[☠️ᴅᴀʀᴋ ʙᴏᴛ ʀᴇᴘᴏ ☠️ ](https://github.com/Harsh-78/Dark-Userbot)\n "    





@bot.on(admin_cmd(outgoing=True, pattern="alive$"))

@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))

async def amireallyalive(alive):

    await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)

    await alive.delete()





    



    
    
