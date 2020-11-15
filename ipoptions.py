from colorama import Fore
import urllib.request   
import json
import os

def banner():
    os.system("clear")
    print(Fore.BLUE + """
  ___           ___           _     _                   
 |_ _|  _ __   / _ \   _ __  | |_  (_)  ___   _ _    ___
  | |  | '_ \ | (_) | | '_ \ |  _| | | / _ \ | ' \  (_-<
 |___| | .__/  \___/  | .__/  \__| |_| \___/ |_||_| /__/
       |_|            |_|                               



  """)
banner()

print(Fore.GREEN + "Version 0.1")

print(Fore.YELLOW + "1. Ip info")
print("2. Keylogger")

opc = int(input(Fore.RED + ">"))

if opc == 1:
    ip = str(input("IP: " + "\n>"))
    url = "https://ipinfo.io/"+ip+"/json"
    
    r = urllib.request.urlopen(url)

    load = json.load(r)

    ipinfo = load["ip"]
    pais = load["country"]
    comunidad = load["region"]
    ciudad = load["city"]
    compania = load["org"]
    timezone = load["timezone"]
    postal = load["postal"]

    print(Fore.MAGENTA + "\n" + "-" * 60)
    print(Fore.GREEN + " " * 23 + ipinfo)
    print(Fore.MAGENTA + "-" * 60 + "\n")

    print(Fore.CYAN + "-" * 60)
    print(Fore.YELLOW + "Pais: " + pais)
    print("Comunidad Autonoma: " + comunidad)
    print("Ciudad: " + ciudad)
    print("Compania: " + compania)
    print("Zona horaria: " + timezone)
    print("Codigo postal: " + postal)

    print(Fore.MAGENTA + "\n" + "-" * 60)
    print("\n")

