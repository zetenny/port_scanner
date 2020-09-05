#!/usr/bin/python3

import socket
import time
from tqdm import tqdm
import colorama
from colorama import Fore, Style

ip = input('target host: ')
scan_range_min, scan_range_max = input('range(min max): ').split()
lista = []

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connect = s.connect((ip, port))
        lista.append(port)
        connect.close()
    except:
        pass

start = time.perf_counter()

for i in tqdm(range(int(scan_range_min), int(scan_range_max))):
    if scan(i):
        pass

finish = time.perf_counter()
print(f'\n Scan time: {round(finish-start, 2)}seconds \n')

for i in lista:
    print(f'Port {Fore.GREEN}{i}{Style.RESET_ALL} is open!')

print()

closed_ports = int(scan_range_max) - len(lista)
print(f'{Fore.RED}{closed_ports}{Style.RESET_ALL} scanned ports are closed or filtered!')
