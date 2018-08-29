###############################################################################
# Task: Take a list of IP Addresses and perform a DNS lookup against them  
#       
#
# Usage: 'python3 dns-lookup.py' The IPs.txt file should be in the root
#        of C:\. Change be changed to Linux using /home/username/....
#
# 
# Author: Collin Clark
# Date: 05JUNE2018
# Version: 1.0
################################################################################

import socket

with open('C:\\IPs.txt') as f:
    for ip in f:
        out = socket.gethostbyaddr(ip)
        print (out[2],out[0])
