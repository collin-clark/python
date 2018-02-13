#!/usr/bin/python
 
# Demo server to open a port
# Modified from Python tutorial docs
import socket
import subprocess

print "---------------------------------------------------------"
print "This script will open any TCP port that is not currently"
print "in use. Below are the ports in use. Any port < 1024 will"
print "require sudo."
print "---------------------------------------------------------"
print " "

# subprocess.check_output(['netstat', '-tulpn', '| grep tcp$'])

what_port = int(raw_input("What port do you want the server to run on? "))

HOST = '127.0.0.1'       # Hostname to bind
PORT = what_port         # Open non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
