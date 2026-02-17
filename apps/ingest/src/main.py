import typer
import asyncio
from datetime import datetime, timedelta, timezone
from rich import print

from src.adapters.usgs import USGSClient


app = typer.Typer()

@app.command()
def fetch_sample():
    async def run():
        client = USGSClient()
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=1)
        
        print(f"[bold green]Fetching earthquakes from {start} to {end}...[/bold green]")
        try:
            data = await client.get_earthquakes(start, end)
            print(f"Found [bold cyan]{data.metadata['count']}[/bold cyan] earthquakes.")
            print("\n[bold]Top 5 most recent:[/bold]")
            sorted_features = sorted(data.features, key=lambda f: f.properties.time, reverse=True)
            
            for feature in sorted_features[:5]:
                props = feature.properties
                time_str = props.time_as_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
                print(f"- [yellow]{time_str}[/yellow]: {props.title} (Mag: {props.mag})")
                
        except Exception as e:
            print(f"[bold red]Error:[/bold red] {e}")

    asyncio.run(run())

@app.command()
def serve():
    print("Starting server... (Not implemented yet)")

if __name__ == "__main__":
    app()
