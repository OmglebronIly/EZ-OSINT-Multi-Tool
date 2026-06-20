from rich.console import Console
from rich.table import Table
import webbrowser

console = Console()

DORKS = {
    "Login Pages": 'intitle:"login" "{}"',
    "Admin Panels": 'intitle:"admin" "{}"',
    "Directory Listings": 'intitle:"index of" "{}"',
    "PDF Files": 'filetype:pdf "{}"',
    "DOCX Files": 'filetype:docx "{}"',
    "TXT Files": 'filetype:txt "{}"',
    "SQL Files": 'filetype:sql "{}"',
    "Config Files": 'ext:conf "{}"',
    "Exposed Env Files": 'ext:env "{}"',
    "Public Cameras": 'inurl:"/view.shtml" "{}"',
}

def run():
    keyword = input("Enter keyword/target: ").strip()

    table = Table(title=f"Dorking Engine: {keyword}")
    table.add_column("Category")
    table.add_column("Dork Query")

    for category, query in DORKS.items():
        dork = query.format(keyword)
        table.add_row(category, dork)

    console.print(table)

    open_choice = input