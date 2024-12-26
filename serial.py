import subprocess
import sys
import platform
import os
import msvcrt
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

def get_disk_drives():
    clear_screen()
    display_ascii_art()
    print("\nDisk Drives Info:")
    command = "wmic diskdrive get model, serialnumber, mediaType, size /format:list"
    print(run_command(command))

def get_cpu_info():
    clear_screen()
    display_ascii_art()
    print("\nCPU Info:")
    command = "wmic cpu get name, manufacturer, maxclockspeed, numberofcores, serialnumber /format:list"
    print(run_command(command))

def get_bios_info():
    clear_screen()
    display_ascii_art()
    print("\nBIOS Info:")
    command = "wmic bios get manufacturer, version, serialnumber, smbiosbiosversion /format:list"
    print(run_command(command))

def get_motherboard_info():
    clear_screen()
    display_ascii_art()
    print("\nMotherboard Info:")
    command = "wmic baseboard get product, manufacturer, version, serialnumber /format:list"
    print(run_command(command))

def get_uuid():
    clear_screen()
    display_ascii_art()
    print("\nSystem UUID:")
    command = "wmic csproduct get uuid"
    print(run_command(command))

def get_mac_addresses():
    clear_screen()
    display_ascii_art()
    print("\nMAC Addresses:")
    command = "getmac /v /fo list"
    print(run_command(command))

def get_system_info():
    clear_screen()
    display_ascii_art()
    print("\nSystem Info:")
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    for key, value in system_info.items():
        print(f"{key}: {value}")

def display_ascii_art():
    ascii_art = Fore.RED + Style.BRIGHT + r"""
╔╦╗╔═╗╔═╗╔╦╗╦ ╦╦═╗╔╗ ╔═╗╔╦╗╦╔═╗╔╗╔  ╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
║║║╠═╣╚═╗ ║ ║ ║╠╦╝╠╩╗╠═╣ ║ ║║ ║║║║  ║║║╠═╣ ║ ║║ ║║║║
╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╝╚╝╩ ╩ ╩ ╩╚═╝╝╚╝ 
    """
    print(ascii_art)

def set_cmd_title():
    subprocess.run("title 765 MN - Serial Checker", shell=True)

def clear_screen():
    os.system("cls")

def wait_for_enter():
    print(Fore.RED + "\nPress Enter to return to the menu...")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                break

def main_menu():
    set_cmd_title()
    while True:
        clear_screen()
        display_ascii_art()
        print("Options:")
        print("[1] Get Disk Drives")
        print("[2] Get CPU Info")
        print("[3] Get BIOS Info")
        print("[4] Get Motherboard Info")
        print("[5] Get System UUID Info")
        print("[6] Get MAC Addresses")
        print("[7] Get System Information")
        print("[8] Exit 765 Serial Checker")

        choice = input("Choose an option: ")

        if choice == "1":
            get_disk_drives()
        elif choice == "2":
            get_cpu_info()
        elif choice == "3":
            get_bios_info()
        elif choice == "4":
            get_motherboard_info()
        elif choice == "5":
            get_uuid()
        elif choice == "6":
            get_mac_addresses()
        elif choice == "7":
            get_system_info()
        elif choice == "8":
            print("Exiting HWID Checker. Thank you!")
            sys.exit()
        else:
            print("Invalid input, Try again.")

        wait_for_enter()

if __name__ == "__main__":
    main_menu()