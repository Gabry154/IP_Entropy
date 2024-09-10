import time
import subprocess
import os
import argparse

# Version of the script
VERSION = "1.0.0"

# Argument parser setup
parser = argparse.ArgumentParser(description="IP Entropy Script")
parser.add_argument('-v', '--version', action='store_true', help="Show the version of the script")
args = parser.parse_args()

# If -v or --version is provided, print the version and exit
if args.version:
    print(f"IP Entropy Script - Version {VERSION}")
    exit()

# Function to check and install packages
def install_package(check_command, install_command, package_name):
    try:
        subprocess.check_output(check_command, shell=True)
        print(f'[+] {package_name} is already installed')
    except subprocess.CalledProcessError:
        print(f'[+] {package_name} is not installed')
        subprocess.check_output('sudo apt update', shell=True)
        subprocess.check_output(install_command, shell=True)
        print(f'[!] {package_name} installed successfully')

# Check if pip3 is installed
install_package('dpkg -s python3-pip', 'sudo apt install python3-pip -y', 'pip3')

# Check if requests is installed
try:
    import requests
except ImportError:
    print('[+] The requests module is not installed')
    os.system('pip3 install requests requests[socks]')
    print('[!] The requests module has been installed')

# Check if Tor is installed
install_package('which tor', 'sudo apt install tor -y', 'Tor')

# Function to get the public IP address using Tor
def get_ip():
    url = 'https://icanhazip.com/'
    try:
        response = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
        return response.text.strip()  # Return only the IP address
    except requests.RequestException as e:
        print(f"[!] Error retrieving IP: {e}")
        return "No IP available"

# Function to change the IP address
def change_ip():
    os.system("service tor reload")
    new_ip = get_ip()
    if "No IP available" not in new_ip:
        print(f'[+] Your IP has been changed: {new_ip}')
    else:
        print('[!] Unable to retrieve the new IP')

# Script entry point
def main():
    os.system("clear")
    print('''\033[1;32m

 ██▓ ██▓███     ▓█████  ███▄    █ ▄▄▄█████▓ ██▀███   ▒█████   ██▓███ ▓██   ██▓
▓██▒▓██░  ██▒   ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▓██░  ██▒▒██  ██▒
▒██▒▓██░ ██▓▒   ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▓██░ ██▓▒ ▒██ ██░
░██░▒██▄█▓▒ ▒   ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▒██▄█▓▒ ▒ ░ ▐██▓░
░██░▒██▒ ░  ░   ░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░▒██▒ ░  ░ ░ ██▒▓░
░▓  ▒▓▒░ ░  ░   ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▓▒░ ░  ░  ██▒▒▒ 
 ▒ ░░▒ ░         ░ ░  ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░▒ ░     ▓██ ░▒░ 
 ▒ ░░░             ░      ░   ░ ░   ░        ░░   ░ ░ ░ ░ ▒  ░░       ▒ ▒ ░░  
 ░                 ░  ░         ░             ░         ░ ░           ░ ░     
                                                                      ░ ░                                                                        
    by Gabry154
''')

    # Start Tor service
    os.system("service tor start")

    print("\033[1;32mChange your SOCKS to 127.0.0.1:9050 \n")

    # Ask user for parameters
    time_interval = int(input("[+] Time to change IP (in seconds) [default=60] >> ") or "60")
    change_count = int(input("[+] How many times do you want to change the IP [default=0 for infinite] >> ") or "0")

    print(f'[+] Your current IP is: {get_ip()}')

    if change_count == 0:
        # Infinite loop
        try:
            while True:
                time.sleep(time_interval)
                change_ip()
        except KeyboardInterrupt:
            print('\n[!] Auto Tor closed')
            quit()
    else:
        # Finite loop
        for _ in range(change_count):
            time.sleep(time_interval)
            change_ip()

if __name__ == '__main__':
    main()
