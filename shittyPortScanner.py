## A port scanner built utilizing the socket module ##

import socket, sys, re, time
from datetime import datetime

def IP_addr_checker(HOST):
    '''
    This function uses a regular expression to check if host is a valid IP address
    '''
    
    IP_checker = re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', HOST)

    return(bool(IP_checker))

## Following variables are used in banner ##
banner_length = 60
left_justify_width = 25

## A list for holding the ports to be scanned ##
port_list = list()

## if system arguments are more than 1 ##
if len(sys.argv) > 1:
    
    ## take second argument as host ##
    input_HOST = sys.argv[1]

else:
    
    ## if host wasn't given as an argument, request for it ##
    input_HOST = input("ENTER TARGET'S IP / HOSTNAME: ")

## if system arguments are more than 2 ##
if len(sys.argv) > 2:

    ## pass "-p-" as the third parameter to scan all 65535 ports ##
    if sys.argv[2] == "-p-":

        port_list = range(1,65536)

    else:

        argument_count = 2

        ## This variable remains true until the end of arguments are reached ##
        in_range = True

        while in_range == True:
            
            try:
                
                ## take third argument as port number ##
                port_list.append(int(sys.argv[argument_count]))

                argument_count += 1

            except IndexError:

                in_range = False

                continue

else:

    ## print a blank line ##
    print()
    print("[+] press ENTER for default scan (ports 1 - 1023)")

    ## wait a few seconds before moving to the next line ##
    time.sleep(1)
    
    print("[+] You can also specify certain ports by seperating them with a space.\
    \ni.e 22 23 53 80 etc.")

    ## wait a few seconds before moving to the next line ##
    time.sleep(1)

    print("[+] To scan all ports (1 - 65535), enter -p-")
    
    ## wait a few seconds before moving to the next line ##
    time.sleep(1)

    ## if port wasn't given as an argument, request for it ##
    input_PORT = input("ENTER PORT(S) TO SCAN: ")

    ## split value(s) of input_PORT using " " as a seperator ##
    temporary_list = input_PORT.split(" ")

    for digit in temporary_list:

        if digit == "-p-":

            port_list = range(1,65536)
            continue

        ## check for digits in temporary_list and add them to port_list ##
        elif digit.isdigit(): port_list.append(int(digit))

try:

    ## Resolves the given target address to it's IP address ##
    resolved_addr = socket.gethostbyname(input_HOST)

    ## Check if resolved_addr is "0.0.0.0" or false 
    ## A bit redundant, since the value of target could just have
    ## been set using an if....else statement
    if resolved_addr == "0.0.0.0" or IP_addr_checker(resolved_addr) == False:

        resolved_addr = False

        print("Incorrect IP address format detected...")

        time.sleep(1)

        print("Changing target to default IP address...")

        time.sleep(1)

except socket.gaierror:

    resolved_addr = False

    print("Hostname could not be resolved....")

    time.sleep(1)

    print("Changing target to default IP address...")

    time.sleep(1)

## default host to make connection to, if host is not a valid address ##
default_HOST = '127.0.0.1'

## sets default host if host is not a valid address ##
TARGET = resolved_addr or default_HOST

if port_list == False:
    
    print("Port(s) to scan not provided...")

    time.sleep(1)

    print("Scanning ports 1 - 1023 instead ...")

    time.sleep(1)
    
## set port range as port_list or default ports ##
PORT_RANGE = port_list or range(1,1024)
number_of_open_ports = 0

## add a banner ##
print("=" * banner_length)
print("[+] TARGET:".ljust(left_justify_width),TARGET)
print("[+] PORT(S):".ljust(left_justify_width),PORT_RANGE)
print("[+] TIME STARTED:".ljust(left_justify_width),str(datetime.now()))
print("=" * banner_length)

print(f"Scanning {TARGET}...\nThis might take a while...")

try:
    
    for PORT in PORT_RANGE:
        
        ## socket.AF_INET refers to ipv4, socket.SOCK_STREAM refers to a port ##
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket.setdefaulttimeout(1)

        ## returns an error indicator, 0 if port is open, 1 otherwise ##
        status = s.connect_ex((TARGET,PORT))
          
        if status == 0:

            print(f"Port {PORT} is open")
            number_of_open_ports += 1

        s.close()

except KeyboardInterrupt:
    print("Program Interrupted.\nExiting")
    sys.exit()

except socket.error:
    print("Could not connect to server.\nExiting.")
    sys.exit()

print("=" * banner_length)
print("[+] TIME FINISHED:".ljust(left_justify_width),str(datetime.now()))
print("[+] NO of OPEN PORT(S):".ljust(left_justify_width),number_of_open_ports)
print("=" * banner_length)