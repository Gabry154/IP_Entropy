# IP_Entropy

### About The Project

![ip_entropy](https://github.com/user-attachments/assets/708c2e8b-e058-4adb-a04e-d21507fe33d9)

This script automatically changes your public IP address using the Tor network

### Features
- Automatically changes your public IP via Tor.
- Allows customization of the time interval and number of IP changes.
- Checks for and installs required dependencies (Tor, pip3, requests).
- Useful for maintaining anonymity while browsing or for tasks requiring frequent IP changes.

### Prerequisites
- Linux-based system with sudo access.
- Python 3.x installed.
- Tor installed or installable via the script.
- pip3 installed or installable via the script.

### Installation
- Clone the repository: ```git clone https://github.com/Gabry154/IP_Entropy.git```
  - Install Tor (if not already installed): ```sudo apt install tor```
  - Install Python dependencies manually (if needed): ```pip3 install requests requests[socks]```
 
### Usage
- Enter the folder ```cd IP_Entropy```
- Run the script: ```sudo python3 ipe.py```
- Follow the on-screen prompts to set:
  - Time interval between IP changes (in seconds).
  - Number of IP changes (set to 0 for infinite changes).
- Make sure to configure your application or browser to use the SOCKS proxy at ```127.0.0.1:9050```

# Donation
- BTC: ```bc1qqr3der8w4a72jrtf7e7jq02lxs349aarsx7ufe```
- XMR: ```46fQbACHA3MgW5XJ9cQaDTXLsCnm1p31k7smYVZfiyBvXeGD3BtBWbkJJTUdagLeQW11SsCD9wVEMdzERoJwnWsJLtnYYpu```
