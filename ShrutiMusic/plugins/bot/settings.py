# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatAction, ChatMemberStatus as CMS
from pyrogram.errors import (
    MessageNotModified,
    MessageEmpty,
    ChatAdminRequired,
    UserIsBlocked,
    ChatWriteForbidden,
    FloodWait,
    RPCError,
)
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    VideoChatScheduled,
    ChatMemberUpdated,
)

from ShrutiMusic import app
from ShrutiMusic.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
)
from ShrutiMusic.utils import bot_sys_stats
from ShrutiMusic.utils.decorators.admins import ActualAdminCB
from ShrutiMusic.utils.decorators.language import language, languageCB
from ShrutiMusic.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from ShrutiMusic.utils.inline.start import private_panel
from config import BANNED_USERS, OWNER_ID

import shutil
import asyncio
import re
import random
import config
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

@app.on_message(
    filters.command(["settings", "setting"]) & filters.group & ~BANNED_USERS
)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(app.mention, message.chat.id, message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("settings_helper") & ~BANNED_USERS)
@languageCB
async def settings_cb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer(_["set_cb_5"])
    except:
        pass
    buttons = setting_markup(_)
    return await CallbackQuery.edit_message_text(
        _["setting_1"].format(
            app.mention,
            CallbackQuery.message.chat.id,
            CallbackQuery.message.chat.title,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("settingsback_helper") & ~BANNED_USERS)
@languageCB
async def settings_back_markup(client, CallbackQuery: CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    if CallbackQuery.message.chat.type == ChatType.PRIVATE:
        await app.resolve_peer(OWNER_ID)
        OWNER = OWNER_ID
        buttons = private_panel(_)
        UP, CPU, RAM, DISK = await bot_sys_stats()
        return await CallbackQuery.edit_message_text(
            _["start_2"].format(CallbackQuery.from_user.mention, app.mention, UP, DISK, CPU, RAM),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = setting_markup(_)
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )


mongodb = MongoCli(config.MONGO_DB_URI)
db = mongodb.Anonymous

CHAT_STORAGE = [
    "mongodb+srv://chatbot1:a@cluster0.pxbu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot2:b@cluster0.9i8as.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot3:c@cluster0.0ak9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot4:d@cluster0.4i428.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot5:e@cluster0.pmaap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot6:f@cluster0.u63li.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot7:g@cluster0.mhzef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot8:h@cluster0.okxao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot9:i@cluster0.yausb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot10:j@cluster0.9esnn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
]

VIPBOY = MongoCli(random.choice(CHAT_STORAGE))
chatdb = VIPBOY.Anonymous
chatai = chatdb.Word.WordDb
storeai = VIPBOY.Anonymous.Word.NewWordDb  

sticker_db = db.stickers.sticker
chatbot_settings = db.chatbot_settings

reply = []
sticker = []
LOAD = "FALSE"

# Adult content filter keywords
ADULT_KEYWORDS = [
    "porn", "sex", "nude", "naked", "xxx", "adult", "18+", "nsfw", 
    "dick", "pussy", "boobs", "ass", "fuck", "bitch", "cum", "orgasm"
]

async def load_caches():
    global reply, sticker, LOAD
    if LOAD == "TRUE":
        return
    LOAD = "TRUE"
    reply.clear()
    sticker.clear()
    
    print("🧹 All cache cleaned successfully")
    await asyncio.sleep(1)
    try:
        print("⏳ Loading All Caches...")
        
        reply = await chatai.find().to_list(length=10000)
        print("✅ Replies Loaded Successfully")
        await asyncio.sleep(1)
        
        sticker = await sticker_db.find().to_list(length=None)
        if not sticker:
            sticker_id = "CAACAgUAAxkBAAENzH5nsI3qB-eJNDAUZQL9v3SQl_m-DAACigYAAuT1GFUScU-uCJCWAjYE"
            await sticker_db.insert_one({"sticker_id": sticker_id})
        print("✅ Stickers Loaded Successfully")
        print("🎉 All caches loaded successfully!")
        LOAD = "FALSE"
    except Exception as e:
        print(f"❌ Error loading caches: {e}")
        LOAD = "FALSE"
    return

async def is_chat_enabled(chat_id: int) -> bool:
    chat = await chatbot_settings.find_one({"chat_id": chat_id})
    return chat and chat.get("enabled", False)

async def set_chat_status(chat_id: int, status: bool):
    await chatbot_settings.update_one({"chat_id": chat_id}, {"$set": {"enabled": status}}, upsert=True)

def is_adult_content(text: str) -> bool:
    """Check if text contains adult content"""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ADULT_KEYWORDS)

async def is_adult_sticker(sticker_id: str) -> bool:
    """Basic check for adult stickers - you can enhance this with ML models"""
    # You can implement more sophisticated checks here
    # For now, we'll use a simple blacklist approach
    adult_sticker_ids = [
        # Add known adult sticker IDs here
    ]
    return sticker_id in adult_sticker_ids

@app.on_message(filters.command("chatbot") & filters.group)
async def toggle_chatbot(client: Client, message: Message):
    user = message.from_user
    chat_id = message.chat.id

    # Only admins/owners can use this command
    chat_member = await client.get_chat_member(chat_id, user.id)
    if chat_member.status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
        return await message.reply_text("<b>❌ Only Admin/Owner can use this command!</b>", parse_mode=enums.ParseMode.HTML)

    # Create inline keyboard
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🟢 Enable", callback_data=f"chatbot_on_{chat_id}"),
            InlineKeyboardButton("🔴 Disable", callback_data=f"chatbot_off_{chat_id}")
        ],
        [
            InlineKeyboardButton("📊 Status", callback_data=f"chatbot_status_{chat_id}")
        ]
    ])

    await message.reply_text(
        "<b>🤖 Chatbot Control Panel</b>\n\n"
        "<b>Choose an option:</b>",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML
    )

@app.on_callback_query(filters.regex(r"chatbot_"))
async def chatbot_callback(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    user_id = callback_query.from_user.id
    chat_id = int(data.split("_")[-1])
    action = data.split("_")[1]

    # Check if user is admin
    try:
        chat_member = await client.get_chat_member(chat_id, user_id)
        if chat_member.status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            return await callback_query.answer("❌ Only admins can control chatbot!", show_alert=True)
    except:
        return await callback_query.answer("❌ Error checking permissions!", show_alert=True)

    if action == "on":
        await set_chat_status(chat_id, True)
        await callback_query.edit_message_text(
            "<b>✅ Chatbot Enabled Successfully!</b>\n\n"
            "<b>🎉 Now I will reply to messages in this group.</b>",
            parse_mode=enums.ParseMode.HTML
        )
    
    elif action == "off":
        await set_chat_status(chat_id, False)
        await callback_query.edit_message_text(
            "<b>🚫 Chatbot Disabled Successfully!</b>\n\n"
            "<b>😴 I will not reply to messages in this group now.</b>",
            parse_mode=enums.ParseMode.HTML
        )
    
    elif action == "status":
        enabled = await is_chat_enabled(chat_id)
        status_text = "<b>🟢 ENABLED</b>" if enabled else "<b>🔴 DISABLED</b>"
        await callback_query.edit_message_text(
            f"<b>🤖 Chatbot Status</b>\n\n"
            f"<b>Current Status:</b> {status_text}\n\n"
            f"<b>Chat ID:</b> <code>{chat_id}</code>",
            parse_mode=enums.ParseMode.HTML
        )

async def get_reply(message_text: str):
    global reply
    matched_replies = [reply_data for reply_data in reply if reply_data["word"] == message_text]

    if matched_replies:
         return random.choice(matched_replies)
        
    return random.choice(reply) if reply else None

async def save_reply(original_message: Message, reply_message: Message):
    global reply
    try:
        # Check for adult content before saving
        if original_message.text and is_adult_content(original_message.text):
            return  # Don't save adult content

        reply_data = {
            "word": original_message.text,
            "text": None,
            "check": "none",
        }

        if reply_message.sticker:
            # Check if sticker is adult content
            if await is_adult_sticker(reply_message.sticker.file_id):
                return  # Don't save adult stickers
            reply_data["text"] = reply_message.sticker.file_id
            reply_data["check"] = "sticker"
        elif reply_message.photo:
            reply_data["text"] = reply_message.photo.file_id
            reply_data["check"] = "photo"
        elif reply_message.video:
            reply_data["text"] = reply_message.video.file_id
            reply_data["check"] = "video"
        elif reply_message.audio:
            reply_data["text"] = reply_message.audio.file_id
            reply_data["check"] = "audio"
        elif reply_message.animation:
            reply_data["text"] = reply_message.animation.file_id
            reply_data["check"] = "gif"
        elif reply_message.voice:
            reply_data["text"] = reply_message.voice.file_id
            reply_data["check"] = "voice"
        elif reply_message.text:
            # Check for adult content in reply text
            if is_adult_content(reply_message.text):
                return  # Don't save adult content
            reply_data["text"] = reply_message.text
            reply_data["check"] = "none"

        # Save stickers to sticker database
        if reply_message.sticker:
            sticker_data = {"sticker_id": reply_message.sticker.file_id}
            existing_sticker = await sticker_db.find_one(sticker_data)
            if not existing_sticker:
                await sticker_db.insert_one(sticker_data)
                sticker.append(sticker_data)

        is_chat = await chatai.find_one(reply_data)
        if not is_chat:
            await chatai.insert_one(reply_data)
            reply.append(reply_data)

    except Exception as e:
        print(f"❌ Error in save_reply: {e}")
          
async def reply_message(client, chat_id, bot_id, message_text, message):
    try:
        reply_data = await get_reply(message_text)
        if reply_data:
            response_text = reply_data["text"]
            
            if reply_data["check"] == "sticker":
                await message.reply_sticker(reply_data["text"])
            elif reply_data["check"] == "photo":
                await message.reply_photo(reply_data["text"])
            elif reply_data["check"] == "video":
                await message.reply_video(reply_data["text"])
            elif reply_data["check"] == "audio":
                await message.reply_audio(reply_data["text"])
            elif reply_data["check"] == "gif":
                await message.reply_animation(reply_data["text"])
            elif reply_data["check"] == "voice":
                await message.reply_voice(reply_data["text"])
            else:
                # Send normal text without bold
                await message.reply_text(response_text, disable_web_page_preview=True)

    except (ChatAdminRequired, UserIsBlocked, ChatWriteForbidden, RPCError) as e:
        return
    except Exception as e:
        print(f"❌ Error in reply_message: {e}")
        return

@app.on_message(filters.incoming, group=1)
async def chatbot(client: Client, message: Message):
    global sticker
    bot_id = client.me.id
    
    # Return if chatbot is disabled in group, but always work in DM
    if message.chat.type != enums.ChatType.PRIVATE and not await is_chat_enabled(message.chat.id):
        return

    if not sticker:
        await load_caches()
        return
    
    if not message.from_user or message.from_user.is_bot:
        return
    
    chat_id = message.chat.id
    
    try:
        # Ignore commands
        if message.text and any(message.text.startswith(prefix) for prefix in ["!", "/", "@", ".", "?", "#"]):
            return
          
        if (message.reply_to_message and message.reply_to_message.from_user.id == client.me.id) or (not message.reply_to_message):
            
            if message.text and message.from_user:
                message_text = message.text.lower()
                
                # Check for adult content
                if is_adult_content(message_text):
                    return await message.reply_text("❌ Please avoid sending inappropriate content!")
                
                # Predefined responses - normal text without bold
                if "gn" in message_text or "good night" in message_text:
                    return await message.reply_text(f"🌙 Good Night! Sweet dreams {message.from_user.mention} ✨")
    
                elif "gm" in message_text or "good morning" in message_text:
                    return await message.reply_text(f"☀️ Good Morning ji! {message.from_user.mention} 🌅")
    
                elif "hello" in message_text or "hii" in message_text or "hey" in message_text:
                    return await message.reply_text(f"👋 Hi {message.from_user.mention}! Kaise ho? 😊")
    
                elif "bye" in message_text or "goodbye" in message_text:
                    return await message.reply_text(f"👋 Goodbye! Take care! {message.from_user.mention} 😊")
    
                elif "thanks" in message_text or "thank you" in message_text:
                    return await message.reply_text("😊 Hehe welcome! Always happy to help! 💫")

                else:
                    try:
                        await client.read_chat_history(message.chat.id)
                    except Exception:
                        pass
                    await reply_message(client, chat_id, bot_id, message_text, message)
                    return
        
        # Save replies from users
        if message.reply_to_message:
            await save_reply(message.reply_to_message, message)
            
    except (ChatAdminRequired, UserIsBlocked, ChatWriteForbidden, RPCError) as e:
        return
    except (Exception, asyncio.TimeoutError) as e:
        return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_2"], show_alert=True)
        except:
            return
    if command == "PLAYMODEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_5"], show_alert=True)
        except:
            return
    if command == "PLAYTYPEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_6"], show_alert=True)
        except:
            return
    if command == "AUTHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_3"], show_alert=True)
        except:
            return
    if command == "VOTEANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_8"],
                show_alert=True,
            )
        except:
            return
    if command == "ANSWERVOMODE":
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        try:
            return await CallbackQuery.answer(
                _["setting_9"].format(current),
                show_alert=True,
            )
        except:
            return
    if command == "PM":
        try:
            await CallbackQuery.answer(_["set_cb_2"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "AU":
        try:
            await CallbackQuery.answer(_["set_cb_1"], show_alert=True)
        except:
            pass
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            buttons = auth_users_markup(_, True)
        else:
            buttons = auth_users_markup(_)
    if command == "VM":
        mode = await is_skipmode(CallbackQuery.message.chat.id)
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        buttons = vote_mode_markup(_, current, mode)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("FERRARIUDTI") & ~BANNED_USERS)
@ActualAdminCB
async def addition(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    mode = callback_data.split(None, 1)[1]
    if not await is_skipmode(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(_["setting_10"], show_alert=True)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    if mode == "M":
        final = current - 2
        print(final)
        if final == 0:
            return await CallbackQuery.answer(
                _["setting_11"],
                show_alert=True,
            )
        if final <= 2:
            final = 2
        await set_upvotes(CallbackQuery.message.chat.id, final)
    else:
        final = current + 2
        print(final)
        if final == 17:
            return await CallbackQuery.answer(
                _["setting_12"],
                show_alert=True,
            )
        if final >= 15:
            final = 15
        await set_upvotes(CallbackQuery.message.chat.id, final)
    buttons = vote_mode_markup(_, final, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(
    filters.regex(pattern=r"^(MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def playmode_ans(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = None
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "MODECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            await set_playmode(CallbackQuery.message.chat.id, "Inline")
            Direct = None
        else:
            await set_playmode(CallbackQuery.message.chat.id, "Direct")
            Direct = True
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = False
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "PLAYTYPECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            await set_playtype(CallbackQuery.message.chat.id, "Admin")
            Playtype = False
        else:
            await set_playtype(CallbackQuery.message.chat.id, "Everyone")
            Playtype = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS)
@ActualAdminCB
async def authusers_mar(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "AUTHLIST":
        _authusers = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _authusers:
            try:
                return await CallbackQuery.answer(_["setting_4"], show_alert=True)
            except:
                return
        else:
            try:
                await CallbackQuery.answer(_["set_cb_4"], show_alert=True)
            except:
                pass
            j = 0
            await CallbackQuery.edit_message_text(_["auth_6"])
            msg = _["auth_7"].format(CallbackQuery.message.chat.title)
            for note in _authusers:
                _note = await get_authuser(CallbackQuery.message.chat.id, note)
                user_id = _note["auth_user_id"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name
                    j += 1
                except:
                    continue
                msg += f"{j}➤ {user}[<code>{user_id}</code>]\n"
                msg += f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=_["BACK_BUTTON"], callback_data=f"AU"
                        ),
                        InlineKeyboardButton(
                            text=_["CLOSE_BUTTON"],
                            callback_data=f"close",
                        ),
                    ]
                ]
            )
            try:
                return await CallbackQuery.edit_message_text(msg, reply_markup=upl)
            except MessageNotModified:
                return
    try:
        await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
    except:
        pass
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_)
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("VOMODECHANGE") & ~BANNED_USERS)
@ActualAdminCB
async def vote_change(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
    except:
        pass
    mod = None
    if await is_skipmode(CallbackQuery.message.chat.id):
        await skip_off(CallbackQuery.message.chat.id)
    else:
        mod = True
        await skip_on(CallbackQuery.message.chat.id)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    buttons = vote_mode_markup(_, current, mod)

    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
