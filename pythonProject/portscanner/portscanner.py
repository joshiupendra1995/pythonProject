import socket
from IPy import IP
print("\033[1;31;40m   \n")  # sets console font to white
print("\033[1;36;40m   \n")  # sets below text to cyan color
print(
    "**     **       **    ********   *******  ********  ********     ******   ******     ***    **    ** **    ** ******** ********")
print(
    "**     **       **    **     ** **     ** **     **    **       **    ** **    **   ** **   ***   ** ***   ** **       **     **")
print(
    "**     **       **    **     ** **     ** **     **    **       **       **        **   **  ****  ** ****  ** **       **     **")
print(
    "**     **       **    ********  **     ** ********     **        ******  **       **     ** ** ** ** ** ** ** ******   ********")
print(
    "**     ** **    **    **        **     ** **   **      **             ** **       ********* **  **** **  **** **       **   **")
print(
    "**     ** **    **    **        **     ** **    **     **       **    ** **    ** **     ** **   *** **   *** **       **    **")
print(
    "*******   ******     **         *******  **     **    **        ******   ******  **     ** **    ** **    ** ******** **     **")


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print("\033[1;31;40m   \n")  # sets color to red
        print(f'[+] Port {p} Is Open')
        print("\033[1;37;40m   \n")  # sets color to white
    except:
        pass


print("\033[1;32;40m   \n")
ipaddress = input('[+] Enter Target To Scan: ')
if ',' in ipaddress:
    for ip in ipaddress.split(','):
        converted_ip = check_ip(ip)
        print(f'[+] Scanning Port for ip {converted_ip}')
        for p in range(75, 81):
            scan_port(converted_ip, p)
else:
    converted_ip = check_ip(ipaddress)
    print(f'[+] Scanning Port for ip {converted_ip}')
    for p in range(75, 81):
        scan_port(converted_ip, p)
