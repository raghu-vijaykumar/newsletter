import click
from datetime import datetime, timedelta
from src.newsletter.fetcher import fetch_articles
from src.newsletter.summarizer import summarize_articles_for_date
from src.newsletter.digest import create_daily_digest
from src.newsletter.audio import generate_digest_audio
from src.newsletter.config import get_date_str, get_days_ago


@click.command()
@click.option("--days", default=7, help="Number of days to fetch (default: 7)")
def main(days):
    """Fetch, summarize, and generate audio for daily tech newsletters."""
    click.echo(f"Processing last {days} days...")

    # Fetch articles
    articles_by_date = fetch_articles(days)
    click.echo(f"Fetched articles for {len(articles_by_date)} dates.")

    # Process each date
    for date_str in sorted(articles_by_date.keys()):
        click.echo(f"Processing {date_str}...")

        # Summarize and generate markdown articles
        summaries = summarize_articles_for_date(date_str)
        click.echo(
            f"Summarized {len(summaries)} articles and generated markdown articles."
        )

        # Generate digest
        digest = create_daily_digest(date_str)
        if digest:
            click.echo("Generated digest.")

            # Generate audio
            generate_digest_audio(date_str)
            click.echo("Generated digest audio.")

    click.echo("Done!")


if __name__ == "__main__":
    main()
