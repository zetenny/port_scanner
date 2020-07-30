#!/usr/bin/python3

from progressbar import ProgressBar
from colorama import Fore, Style
import socket
from datetime import datetime

bar = ProgressBar()
def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
    except:
        return False
    else:
        return True
ip = input("TARGET: ")
lista = []
i1 = datetime.now()
for port in bar(range(0, 1025)):    # here you can modify the scan range
    if scan(ip, port):
        lista.append(port)
i2 = datetime.now()
print('\n', 'Scan time: ', i2 - i1, '\n')

for i in lista:
    print('Port ' + Fore.GREEN + str(i) + Style.RESET_ALL + ' is open!')

asd = 1025 - int(len(lista))
print(f'\n The other {Fore.RED}{asd}{Style.RESET_ALL} scanned ports are closed or filtered!')
