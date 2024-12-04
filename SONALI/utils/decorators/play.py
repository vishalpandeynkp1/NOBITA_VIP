import asyncio
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import YouTube, app
from SONALI.misc import SUDOERS
from SONALI.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from SONALI.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

links = {}

def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        
        # Sender Chat Check
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="RAUSHANmousAdmin")]]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)
        
        try:
            await message.delete()
        except Exception:
            pass
        
        # Media Handling
        audio_telegram = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
        video_telegram = (message.reply_to_message.video or message.reply_to_message.document) if message.reply_to_message else None
        url = await YouTube.url(message)
        
        if not audio_telegram and not video_telegram and not url:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(photo=PLAYLIST_IMG_URL, caption=_["play_18"], reply_markup=InlineKeyboardMarkup(buttons))
        
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_7"])
            try:
                chat = await app.get_chat(chat_id)
                channel = chat.title
            except Exception:
                return await message.reply_text(_["cplay_4"])
        else:
            chat_id = message.chat.id
            channel = None
        
        # Playmode Check
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone" and message.from_user.id not in SUDOERS:
            admins = adminlist.get(message.chat.id)
            if not admins or message.from_user.id not in admins:
                return await message.reply_text(_["play_4"])
        
        # Video/Audio Handling
        video = "v" in message.command[0] or "-v" in message.text
        fplay = True if message.command[0][-1] == "e" else None
        
        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                get = await app.get_chat_member(chat_id, userbot.id)
                if get.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
                    return await message.reply_text(_["call_2"].format(app.mention, userbot.id))
            except UserNotParticipant:
                invitelink = links.get(chat_id) or await create_invite_link(app, chat_id, message)
                try:
                    await userbot.join_chat(invitelink)
                except InviteRequestSent:
                    await handle_invite_request(app, chat_id, userbot, message)
                except Exception as e:
                    return await message.reply_text(f"Error: {type(e).__name__}, Details: {e}")
                
                links[chat_id] = invitelink
            
        return await command(client, message, _, chat_id, video, channel, playmode, url, fplay)

    return wrapper

# Helper Functions
async def create_invite_link(app, chat_id, message):
    try:
        return await app.export_chat_invite_link(chat_id)
    except ChatAdminRequired:
        await message.reply_text("Bot needs admin permission to generate invite link.")
        raise

async def handle_invite_request(app, chat_id, userbot, message):
    try:
        await app.approve_chat_join_request(chat_id, userbot.id)
        await asyncio.sleep(3)
        await message.edit_text("Join request approved.")
    except Exception as e:
        await message.reply_text(f"Failed to approve join request: {e}")
