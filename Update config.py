import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = 26125923
API_HASH = "918b6ac7c1735dbc1d2333d424094ddc"
BOT_TOKEN = "6716861481:AAEm1QuJKWbYJfUgD17hws3S44At02l2gAU"
MONGO_DB_URI = "mongodb+srv://prithvisingh7369:laN0ue2TvR0DiH7Y@cluster0.lvdml35.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOGGER_ID = 1002135774887
OWNER_ID = 6280553231

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/allexamquiz125")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/quizopson")

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
STRING1 = ""
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
    "START_IMG_URL", "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
STATS_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
STREAM_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/7eee3ad3c25731e7ef282.jpg"


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
