import os
import winsound
from rich.console import Console
from rich.panel import Panel

console = Console()

from modules import (
    Ip_lookup,
    Username_lookup,
    Email_lookup,
    Phone_lookup,
    Wallet_lookup,
    Dorking,
    File_metadata_scan,
    file_metadata_delete,
    website_cloner,
    ip_pinger,
    geo_locator
)

def banner():
    console.print(Panel.fit(
        """[bold purple]
 __   __         ___    ___  __   __       
/  \ /__` | |\ |  |  __  |  /  \ /  \ |    
\__/ .__/ | | \|  |      |  \__/ \__/ |___ 
                                           

        [bright_white]EZ_OSINT Multitool[/bright_white]
[/bold purple]""",
        title="[bright_white]Hybrid Hacker Mode[/bright_white]",
        border_style="purple"
    ))

def menu():
    console.print("""
[bold bright_white][H][/bold bright_white] Help    [bold bright_white][V][/bold bright_white] Version    [bold bright_white][S][/bold bright_white] Settings    [bold bright_white][C][/bold bright_white] Credits

[bold purple][Pentesting][/bold purple]                 [bold purple][Utilities][/bold purple]                     [bold purple][Tools][/bold purple]
[bright_white]01[/bright_white] IP Lookup               [bright_white]08[/bright_white] File Metadata Scan         [bright_white]11[/bright_white] IP Pinger
[bright_white]02[/bright_white] Username Lookup         [bright_white]09[/bright_white] File Metadata Delete       [bright_white]12[/bright_white] Geo Locator
[bright_white]03[/bright_white] Email Lookup            [bright_white]10[/bright_white] Website Cloner             [bright_white]13[/bright_white] Recent Lookups
[bright_white]04[/bright_white] Phone Lookup
[bright_white]05[/bright_white] Wallet Tracker
[bright_white]06[/bright_white] Dorking Engine

[bold purple][System][/bold purple]
[bright_white]00[/bright_white] Exit
""")

def main():
    winsound.Beep(600, 200)
    winsound.Beep(800, 200)

    while True:
        os.system("cls")
        banner()
        menu()

        console.print("[bold purple](RLC@LOsint-Tool)~[C:\\Osint][/bold purple]")
        choice = input("$ ").strip()

        if choice == "01":
            Ip_lookup.run()
        elif choice == "02":
            Username_lookup.run()
        elif choice == "03":
            Email_lookup.run()
        elif choice == "04":
            Phone_lookup.run()
        elif choice == "05":
            Wallet_lookup.run()
        elif choice == "06":
            Dorking.run()
        elif choice == "08":
            File_metadata_scan.run()
        elif choice == "09":
            file_metadata_delete.run()
        elif choice == "10":
            website_cloner.run()
        elif choice == "11":
            ip_pinger.run()
        elif choice == "12":
            geo_locator.run()
        elif choice == "13":
            import modules.recent as recent
            recent.show_recent()
        elif choice == "14":
            import modules.recent as recent
            recent.clear_recent()
        elif choice.upper() == "S":
            import modules.settings as settings
            settings.run()
        elif choice.upper() == "C":
            console.print("""
[bold purple]=== Credits ===[/bold purple]

[bright_white]Made by:[/bright_white] rlc
[bright_white]Theme:[/bright_white] Hybrid Hacker Purple
[bright_white]Powered by:[/bright_white] Python 3
[bright_white]Version:[/bright_white] 1.0.0
""")
            input("\nPress ENTER...")
        elif choice.upper() == "V":
            console.print("\n[bright_white]EASY-OSINT Multitool v1.0.0[/bright_white]")
            input("\nPress ENTER...")
        elif choice.upper() == "H":
            console.print("\n[cyan]Use numbers to select tools. S = Settings, C = Credits, 13 = Recent Lookups.[/cyan]")
            input("\nPress ENTER...")
        elif choice == "00":
            break
        else:
            console.print("[red]Invalid option[/red]")
            input("\nPress ENTER...")

if __name__ == "__main__":
    main()
