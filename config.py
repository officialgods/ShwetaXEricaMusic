import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23255238"))
API_HASH = getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002401739175))

OWNER_ID = int(getenv("OWNER_ID", 7825870013))

OWNER = int(getenv("OWNER", 7825870013))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-244ce902-f5e3-4c52-94d6-b5c4bb4ab7e5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SONGSONG220/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_SOULMATES_HUB")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+dtFI4SrfNO5iMTNl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

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


START_IMG_URL = getenv("START_IMG_URL", "https://i.imghippo.com/files/mFmE6428fx.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.imghippo.com/files/mFmE6428fx.jpg")
PLAYLIST_IMG_URL = "https://i.imghippo.com/files/MM9837Mjo.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.imghippo.com/files/mFmE6428fx.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/hygnc6.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/hygnc6.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
