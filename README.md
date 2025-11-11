# Newsletter Daily Digest

A Python CLI tool to fetch daily newsletters from tech blogs, summarize them using Gemini LLM, and generate audio digests.

## Features

- Fetches articles from RSS feeds of reputed tech blogs
- Summarizes articles using LangChain and Google Gemini
- Generates daily digests
- Creates audio versions using Google Text-to-Speech
- Rate limiting for LLM calls
- Skips already processed data on reruns
- Configurable number of days to fetch

## Setup

1. Install uv if not already installed.
2. Clone or download the project.
3. Install dependencies: `uv sync`
4. Set up environment variable: Copy `.env.example` to `.env` and add your Google API key.

## Usage

Run the CLI:

```bash
uv run python main.py --days 7
```

This will fetch articles from the last 7 days, summarize them, generate digests, and create audio files.

Data is stored in the `data/` directory, organized by date.

## Sources

Currently configured for:
- TechCrunch
- Ars Technica
- The Verge
- MIT Technology Review
- Wired

## Requirements

- Python 3.12+
- Google API key for Gemini
- Internet connection for fetching RSS and API calls
