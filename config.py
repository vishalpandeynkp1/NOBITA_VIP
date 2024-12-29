import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_NOBITA_BOT_DEVLOPER_ll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME", "aaru_music_xbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------

AUTO_GCAST = getenv("AUTO_GCAST", "On")

AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", None)
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "17000"))

# Chat id or username of a group for logging bot's activities
LOGGER_ID = getenv("LOGGER_ID", "-1001511253627")

# Logic to handle both numeric IDs and usernames
if LOGGER_ID.isdigit() or (LOGGER_ID.startswith("-") and LOGGER_ID[1:].isdigit()):
    LOGGER_ID = int(LOGGER_ID)  # Convert to integer if it's a numeric ID
else:
    LOGGER_ID = LOGGER_ID  # Keep as string if it's a username

LOG_GROUP_ID = LOGGER_ID

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7708051264"))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vishalpandeynkp1/NOBITA_VIP",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NOBITA_ALL_BOT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/9uused.webp"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/9uused.webp"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/9uused.webp"
STATS_IMG_URL = "https://files.catbox.moe/9uused.webp"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/9uused.webp"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/9uused.webp"
STREAM_IMG_URL = "https://files.catbox.moe/9uused.webp"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/9uused.webp"
YOUTUBE_IMG_URL = "https://files.catbox.moe/9uused.webp"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/9uused.webp"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/9uused.webp"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/9uused.webp"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
