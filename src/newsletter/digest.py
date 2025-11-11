import json
import os
import time
from langchain_core.prompts import PromptTemplate
from tenacity import retry, stop_after_attempt, wait_fixed
from .clients import get_llm
from .config import DATA_DIR, RATE_LIMIT_RPM, last_llm_call

# Rate limiting
wait_time = 60 / RATE_LIMIT_RPM


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(wait_time),
)
def generate_digest(summaries):
    """Generate a daily digest from article summaries."""
    global last_llm_call
    current_time = time.time()
    time_since_last = current_time - last_llm_call
    if time_since_last < wait_time:
        time.sleep(wait_time - time_since_last)

    llm = get_llm()

    if not summaries:
        return "No articles to summarize for this day."

    summaries_text = "\n\n".join([f"- {s['title']}: {s['summary']}" for s in summaries])

    prompt = PromptTemplate.from_template(
        "Create a concise daily digest of the following tech news summaries. Organize by themes if possible, and highlight the most important stories:\n\n{summaries}\n\nDaily Digest:"
    )
    chain = prompt | llm
    response = chain.invoke({"summaries": summaries_text})
    last_llm_call = time.time()
    return response.content.strip()


def create_daily_digest(date_str):
    """Create and save daily digest for a date."""
    date_dir = os.path.join(DATA_DIR, date_str)
    summaries_file = os.path.join(date_dir, "summaries.json")
    digest_file = os.path.join(date_dir, "digest.txt")

    if os.path.exists(digest_file):
        print(f"Digest already exists for {date_str}, skipping.")
        with open(digest_file, "r") as f:
            return f.read()

    if not os.path.exists(summaries_file):
        print(f"No summaries found for {date_str}")
        return None

    with open(summaries_file, "r") as f:
        summaries = json.load(f)

    digest = generate_digest(summaries)

    with open(digest_file, "w") as f:
        f.write(digest)

    return digest
