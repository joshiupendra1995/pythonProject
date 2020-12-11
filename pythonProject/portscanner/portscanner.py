import socket
from IPy import IP

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


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + f'[ - 0 Scanning Target] {target}')
    for port in range(port_start_range, port_end_range):
        scan_port(converted_ip, port)


def get_banner(s):
    return s.recv(1024)


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
        try:
            banner = get_banner(sock)
            print("\033[1;36;40m   \n")
            print('\n' + f'[+] Port {port} Is Open :' + str(banner.decode().strip('\n')))
            print("\033[1;37;40m   \n")  # sets console font to white
        except:
            print('\n' + f'[+] Port {port} Is Open :')
    except:
        pass
        # print("\033[1;31;40m   \n")  # sets color to red
        # print('\n'+f'[-] Port {port} Is Closed')


print("\033[1;32;40m   \n")
ipaddress = input('[+] Enter Target To Scan: ')
port_start_range = int(input('[+] Enter The Port Start Range To Scan: '))
port_end_range = int(input('[+]Enter The Port End Range To Scan: '))
if ',' in ipaddress:
    for ip in ipaddress.split(','):
        scan(ip)
else:
    scan(ipaddress)
