import requests
import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

API_KEY = "YOUR_API_KEY_HERE"

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
        console.print(f"[cyan]Checking{'.' * i}[/cyan]", end="\r")
        time.sleep(0.25)

def run():
    console.print("\n[bold purple]=== Phone Lookup ===[/bold purple]")
    phone = input("Enter phone number: ").strip()

    loading()

    url = f"https://api.apilayer.com/number_verification/validate?number={phone}"
    headers = {"apikey": API_KEY}
    r = requests.get(url, headers=headers)
    data = r.json()

    console.print("\n[bold purple]Results:[/bold purple]")
    for k, v in data.items():
        color = "green" if v not in (None, "", False) else "red"
        console.print(f"[blue]{k}[/blue]: [{color}]{v}[/{color}]")

    save = input("\nSave results as JSON? (y/n): ").lower()
    if save == "y":
        save_json(data, "PhoneLookup")

    from modules.recent import add_recent
    add_recent("Phone Lookup", phone)
