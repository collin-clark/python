###############################################################################
# Task: Ping hosts listed in a text file and report up/down status. If it is  
#       up it will try and reverse DNS to get the hostname.
#
# Usage: 'python3 ping-hosts.py' The ping-hosts.txt file should be in the same
#        directory as this script.
#
# 
# Author: Collin Clark
# Date: 03MAY2018
# Version: 1.0
################################################################################

import os
import platform
import socket


# Open the ping-hosts.txt file and read each line as a string
with open("ping-hosts.txt") as fp:
    hostname = fp.readline()
    for hostname in fp:
    
    		# Lets remove /n from the string	
        hostname = hostname.rstrip()
        # Ping based on Windows or Unix    
        if platform.system() == "Windows":
            response = os.system("ping "+hostname+" -n 1")
        else:
            response = os.system("ping -c 1 " + hostname)
            print(hostname)
        # A boolean on whether or not the host responded to the ping
        if response == 0:
        	  # Let's grab the DNS info for the IP above
            dns_raw = socket.gethostbyaddr(hostname)
            # gethostbyaddr returns a tuple of information. All we need is the first one.
            slice = dns_raw[0]
            print("The host "+hostname+" is UP and its hostname is "+slice)
        else:
            print(hostname+" is down")


