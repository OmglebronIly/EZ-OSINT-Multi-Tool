import json
import os
from rich.console import Console

console = Console()

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "auto_save_json": False,
    "auto_log_recent": True,
    "theme": "hybrid"
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def run():
    settings = load_settings()

    console.print("\n[bold purple]=== Settings ===[/bold purple]")
    console.print(f"[bright_white]1.[/bright_white] Toggle Auto-Save JSON (currently: [cyan]{settings['auto_save_json']}[/cyan])")
    console.print(f"[bright_white]2.[/bright_white] Toggle Recent Logging (currently: [cyan]{settings['auto_log_recent']}[/cyan])")
    console.print(f"[bright_white]3.[/bright_white] Theme (currently: [cyan]{settings['theme']}[/cyan])")
    console.print("[bright_white]0.[/bright_white] Back")

    choice = input("\nSelect: ").strip()

    if choice == "1":
        settings["auto_save_json"] = not settings["auto_save_json"]
    elif choice == "2":
        settings["auto_log_recent"] = not settings["auto_log_recent"]
    elif choice == "3":
        settings["theme"] = "hybrid" if settings["theme"] != "hybrid" else "purple"

    save_settings(settings)
    console.print("\n[green]Settings updated.[/green]")
    input("\nPress ENTER...")
