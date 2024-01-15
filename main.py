import socket #libary for the socket functions
import os #libary for the operating system functions
import time #Libary for the time functions
import sys #Libary that provides access to system-specific parameters and functions.


def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

HOST = "0.0.0.0"  #possible ips in order to connect to the machine 0.0.0.0 meaning everyone who's in the same network as the machine.
PORT = 4444       #The port that the code is listing to.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f'[+] Listening for connections on host: {HOST}, port: {PORT}')

while True:
    conn, address = s.accept()
    print(f'[+] Connection established from {address}')
    time.sleep(5)
    sleep()
    sys.exit()





