import requests
import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

SITES = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Twitter/X": "https://x.com/{}",
    "Reddit": "https://www.reddit.com/user/{}/",
    "TikTok": "https://www.tiktok.com/@{}"
}

def save_json(data, name_prefix):
    folder = "Output"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{name_prefix}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    console.print(f"\n[cyan]Saved as:[/cyan] [bright_white]{filename}[/bright_white]")

def loading():
    import time
    for i in range(3):
        console.print(f"[cyan]Scanning{'.' * i}[/cyan]", end="\r")
        time.sleep(0.25)

def run():
    console.print("\n[bold purple]=== Username Lookup ===[/bold purple]")
    username = input("Enter username: ").strip()
    results = {}

    loading()

    for platform, url in SITES.items():
        check_url = url.format(username)
        try:
            r = requests.get(check_url, timeout=5)
            if r.status_code == 200:
                console.print(f"[green]FOUND[/green] [bright_white]{platform}[/bright_white] → [cyan]{check_url}[/cyan]")
                results[platform] = "FOUND"
            elif r.status_code == 404:
                console.print(f"[red]NOT FOUND[/red] [bright_white]{platform}[/bright_white]")
                results[platform] = "NOT FOUND"
            else:
                console.print(f"[yellow]UNKNOWN[/yellow] [bright_white]{platform}[/bright_white]")
                results[platform] = "UNKNOWN"
        except:
            console.print(f"[red]ERROR[/red] [bright_white]{platform}[/bright_white]")
            results[platform] = "ERROR"

    results["username"] = username

    save = input("\nSave results as JSON? (y/n): ").lower()
    if save == "y":
        save_json(results, "UsernameLookup")

    from modules.recent import add_recent
    add_recent("Username Lookup", username)
