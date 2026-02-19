import asyncio
from datetime import UTC, datetime, timedelta

import typer
from rich import print

app = typer.Typer()


@app.command()
def fetch_sample():
    async def run():
        end = datetime.now(UTC)
        start = end - timedelta(days=1)

        from src.adapters.db import AsyncSessionLocal
        from src.service.ingest import IngestService

        print(f"[bold green]Starting pipeline run from {start} to {end}...[/bold green]")

        try:
            async with AsyncSessionLocal() as session:
                service = IngestService(session)
                saved = await service.fetch_and_store_range(start, end)
                print(f"[bold cyan]Pipeline run complete. {len(saved)} earthquakes processed.[/bold cyan]")

                print("\n[bold]Top 5 most recent stored:[/bold]")
                sorted_saved = sorted(saved, key=lambda f: f.time, reverse=True)
                for eq in sorted_saved[:5]:
                    time_str = eq.time_as_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
                    print(f"- [yellow]{time_str}[/yellow]: {eq.title} (Mag: {eq.mag})")

        except Exception as e:
            print(f"[bold red]Error:[/bold red] {e}")
            import traceback

            traceback.print_exc()

    asyncio.run(run())


if __name__ == "__main__":
    app()
