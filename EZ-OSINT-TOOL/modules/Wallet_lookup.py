import requests
import json
import os
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
        console.print(f"[cyan]Querying{'.' * i}[/cyan]", end="\r")
        time.sleep(0.25)

def run():
    console.print("\n[bold purple]=== Wallet Lookup ===[/bold purple]")
    wallet = input("Enter crypto wallet address: ").strip()

    loading()

    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet}"
    r = requests.get(url)
    data = r.json()

    console.print("\n[bold purple]Results:[/bold purple]")
    for k, v in data.items():
        console.print(f"[blue]{k}[/blue]: [bright_white]{v}[/bright_white]")

    save = input("\nSave results as JSON? (y/n): ").lower()
    if save == "y":
        save_json(data, "WalletLookup")

    from modules.recent import add_recent
    add_recent("Wallet Lookup", wallet)
