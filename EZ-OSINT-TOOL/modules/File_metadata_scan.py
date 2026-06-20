import os
from rich.console import Console
from rich.table import Table

console = Console()

def run():
    path = input("Enter file path: ").strip()

    if not os.path.isfile(path):
        console.print("[red]File not found[/red]")
        return

    stats = os.stat(path)

    table = Table(title=f"Metadata: {path}")
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Size (bytes)", str(stats.st_size))
    table.add_row("Created", str(stats.st_ctime))
    table.add_row("Modified", str(stats.st_mtime))
    table.add_row("Accessed", str(stats.st_atime))

    console.print(table)
