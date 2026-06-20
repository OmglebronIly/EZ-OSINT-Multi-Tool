import os
import json
from datetime import datetime
from rich.console import Console

console = Console()

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
        console.print(f"[cyan]Pinging{'.' * i}[/cyan]", end="\r")
        time.sleep(0.25)

def run():
    console.print("\n[bold purple]=== IP Pinger ===[/bold purple]")
    target = input("Enter IP or domain to ping: ").strip()

    loading()

    response = os.popen(f"ping {target}").read()
    console.print(f"\n[bright_white]{response}[/bright_white]")

    data = {"target": target, "response": response}

    save = input("\nSave results as JSON? (y/n): ").lower()
    if save == "y":
        save_json(data, "IpPinger")

    from modules.recent import add_recent
    add_recent("IP Pinger", target)
