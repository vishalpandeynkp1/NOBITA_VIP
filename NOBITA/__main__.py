import asyncio
import importlib

from pyrogram import idle

import config
from NOBITA import LOGGER, app, userbot
from NOBITA.core.call import NOBI
from NOBITA.misc import sudo
from NOBITA.plugins import ALL_MODULES
from NOBITA.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "ꜱᴛʀɪɴɪɴɢ ✨ ꜱᴇꜱꜱɪᴏɴ 🔒 ɴᴏᴛ ꜰɪʟʟᴇᴅ, ᴘʟᴇᴀꜱᴇ 📝 ꜰɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ 🖥️ v2 🛠️ ꜱᴇꜱꜱɪᴏɴ."
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NOBITA.plugins" + all_module)
    LOGGER("NOBITA.plugins").info("ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ʟᴏᴀᴅᴇᴅ ʙᴀʙʏ 🥳🎉🚀")
    await userbot.start()
    await NOBI.start()
    await NOBI.decorators()
    LOGGER("NOBITA").info("꘎♡━━━━━♡꘎\n  ♨️𝐄𝐒𝐀𝐊𝐎 𝐍𝐎𝐁𝐈𝐓𝐀 𝐏𝐀𝐏𝐀 𝐍𝐄 𝐁𝐀𝐍𝐀𝐘𝐀 𝐇♨️\n꘎♡━━━━━♡꘎")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NOBITA").info("꘎♡━━━━━♡꘎\n  ♨️𝐄𝐒𝐀𝐊𝐎 𝐍𝐎𝐁𝐈𝐓𝐀 𝐏𝐀𝐏𝐀 𝐍𝐄 𝐁𝐀𝐍𝐀𝐘𝐀 𝐇♨️\n꘎♡━━━━━♡꘎")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
