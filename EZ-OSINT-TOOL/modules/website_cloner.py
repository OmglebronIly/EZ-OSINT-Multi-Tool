import requests
from rich.console import Console

console = Console()

def run():
    url = input("Enter website URL: ").strip()
    filename = input("Save as (example: site.html): ").strip()

    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            console.print("[red]Failed to fetch website[/red]")
            return

        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)

        console.print(f"[green]Website saved as {filename}[/green]")

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
