import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

RECENT_FILE = "recent.json"

ICONS = {
    "IP Lookup": "📍",
    "Username Lookup": "👤",
    "Email Lookup": "✉️",
    "Phone Lookup": "📱",
    "Wallet Lookup": "💰",
    "Geo Locator": "🌍",
    "IP Pinger": "📡"
}

def add_recent(entry_type, value):
    data = []

    if os.path.exists(RECENT_FILE):
        with open(RECENT_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.insert(0, {
        "type": entry_type,
        "value": value,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    data = data[:10]

    with open(RECENT_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_recent():
    if not os.path.exists(RECENT_FILE):
        console.print("\n[red]No recent lookups found.[/red]")
        input("\nPress ENTER...")
        return

    with open(RECENT_FILE, "r") as f:
        data = json.load(f)

    console.print("\n[bold purple]=== Recent Lookups ===[/bold purple]\n")

    for item in data:
        icon = ICONS.get(item["type"], "➡️")
        console.print(
            f"{icon} [bold purple]{item['type']}[/bold purple] "
            f"[bright_white]{item['value']}[/bright_white] "
            f"[dim]{item['time']}[/dim]"
        )

    input("\nPress ENTER...")

def clear_recent():
    if os.path.exists(RECENT_FILE):
        os.remove(RECENT_FILE)
        console.print("\n[green]Recent lookups cleared.[/green]")
    else:
        console.print("\n[cyan]No recent file to clear.[/cyan]")
    input("\nPress ENTER...")
