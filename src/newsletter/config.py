import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Sources: list of RSS feed URLs for tech company blogs
SOURCES = [
    "https://developers.googleblog.com/feeds/posts/default",
    "https://research.google/blog/rss/",
    "https://engineering.fb.com/feed/",
    "https://netflixtechblog.com/feed",
    "https://medium.com/feed/airbnb-engineering",
    "https://eng.uber.com/feed/",
    "https://engineering.linkedin.com/blog.rss.html",
    "https://blog.twitter.com/engineering/feed",
    "https://engineering.atspotify.com/feed/",
    "https://dropbox.tech/feed",
    "https://slack.engineering/feed",
    "https://shopify.engineering/rss.xml",
    "https://reddit.engineering/feed.xml",
    "https://medium.com/feed/pinterest-engineering",
    "https://instagram-engineering.com/feed",
    "https://devblogs.microsoft.com/feed/",
    "https://aws.amazon.com/blogs/aws/feed/",
    "https://openai.com/feed.xml",
    "https://github.blog/category/engineering/feed/",
    "https://blog.cloudflare.com/rss/",
    "https://databricks.com/blog/category/engineering/feed",
    "https://www.atlassian.com/engineering/feed.xml",
    "https://stripe.com/blog/engineering/feed",
    "https://discord.com/blog/rss.xml",
    "https://www.notion.so/blog/rss.xml",
    "https://www.canva.dev/blog/engineering/feed",
    "https://doordash.engineering/feed/",
    "https://engineering.grab.com/feed/",
    "https://about.gitlab.com/atom.xml",
    "https://product.hubspot.com/blog/rss.xml",
    "https://www.digitalocean.com/blog/feed.xml",
    "https://blog.heroku.com/engineering/feed.xml",
    "https://www.intel.com/content/www/us/en/developer/articles/blog.rss.xml",
    "https://developer.nvidia.com/blog/feed/",
    "https://medium.com/feed/adobetech",
    "https://engineering.salesforce.com/feed/",
    "https://www.intel.ai/blog/feed/",
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

# Date format
DATE_FORMAT = "%Y-%m-%d"


def get_date_str(date):
    return date.strftime(DATE_FORMAT)


def get_days_ago(days):
    return datetime.now() - timedelta(days=days)


def get_start_of_day(days_ago=0):
    date = datetime.now() - timedelta(days=days_ago)
    return date.replace(hour=0, minute=0, second=0, microsecond=0)
