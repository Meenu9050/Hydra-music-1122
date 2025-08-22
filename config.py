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


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ⚙️ CONFIGURATION FILE | Powered By @WTF_WhyMeeh & @ShrutiBots
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "@GodxSharma")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@HydraxMusic_bot")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠 Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/Meenu9050/Ganna-Music-App-new-")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "Hydrax_Music_update")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Hydrax_Music_update")
INSTAGRAM = os.getenv("INSTAGRAM", "")
YOUTUBE = os.getenv("YOUTUBE", "")
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/ShrutiBots/91")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼 Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
