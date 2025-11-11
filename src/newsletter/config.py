import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Sources: list of RSS feed URLs for tech company blogs
SOURCES = [
    "https://developers.googleblog.com/feeds/posts/default",
    "https://research.google/blog/rss/",
    "https://engineering.fb.com/feed/",
    "https://medium.com/feed/airbnb-engineering",
    "https://engineering.linkedin.com/blog.rss.html",
    "https://engineering.atspotify.com/feed/",
    "https://dropbox.tech/feed",
    "https://slack.engineering/feed",
    "https://medium.com/feed/pinterest-engineering",
    "https://devblogs.microsoft.com/feed/",
    "https://aws.amazon.com/blogs/aws/feed/",
    "https://github.blog/category/engineering/feed/",
    "https://blog.cloudflare.com/rss/",
    "https://www.databricks.com/feed",
    "https://www.atlassian.com/blog/artificial-intelligence/feed",
    "https://discord.com/blog/rss.xml",
    "https://www.canva.dev/blog/engineering/feed",
    "https://doordash.engineering/feed/",
    "https://engineering.grab.com/feed",
    "https://about.gitlab.com/atom.xml",
    "https://www.heroku.com/blog/feed/",
    "https://developer.nvidia.com/blog/feed/",
    "https://medium.com/feed/adobetech",
    "https://engineering.salesforce.com/feed/",
    "https://dropbox.tech/security/feed",
    "https://developer.squareup.com/blog/rss.xml",
]


# API Key from environment
def get_google_api_key():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    return key


def get_groq_api_key():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    return key


def get_telegram_bot_token():
    key = os.getenv("TELEGRAM_BOT_TOKEN")
    if not key:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")
    return key


def get_telegram_chat_id():
    key = os.getenv("TELEGRAM_CHAT_ID")
    if not key:
        raise ValueError("TELEGRAM_CHAT_ID environment variable not set")
    return key


# LLM Provider settings
DEFAULT_LLM_PROVIDER = "gemini"  # Options: "gemini", "groq"
GROQ_MODEL = "openai/gpt-oss-120b"
GEMINI_MODEL = "gemini-2.0-flash"


# Data directory
DATA_DIR = "data"

# Rate limiting: requests per minute for LLM
RATE_LIMIT_RPM = 1  # Adjust as needed

# Rate limiting: requests per minute for gTTS
TTS_RATE_LIMIT_RPM = 1

# Global for LLM rate limiting
last_llm_call = 0

# Audio settings
AUDIO_LANG = "en"
AUDIO_SPEED = 1.25  # Speed multiplier (1.0 = normal speed, 1.25 = 25% faster)

# Date format
DATE_FORMAT = "%Y-%m-%d"


def get_date_str(date):
    return date.strftime(DATE_FORMAT)


def get_days_ago(days):
    return datetime.now() - timedelta(days=days)


def get_start_of_day(days_ago=0):
    date = datetime.now() - timedelta(days=days_ago)
    return date.replace(hour=0, minute=0, second=0, microsecond=0)
