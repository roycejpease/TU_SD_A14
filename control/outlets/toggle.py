#!/usr/bin/env python

#imports
import os
import sys
import subprocess
import json

def main():
#get arguments
    args = sys.argv[1:]

    #fault if arg count incorrect
    if len(args) != 3:
        exit(1)

    channel = int(args[0])
    port = int(args[1])
    option = str(args[2])

    #fault if invalid args
    if(channel > 4 or port > 4 and not (option == 'on' or option == 'off')):
        exit(1)

    #load code arrays
    with open("json/codes_on.json", 'r') as f:
        onCodes = json.load(f)
    with open("json/codes_off.json", 'r') as f:
        offCodes = json.load(f)

    #get the specified code
    if option == 'on':
        code = str(onCodes[channel][port])
    else:
        code = str(offCodes[channel][port])

    #generate and call command to send code
    command = 'codesend ' + code + ' -l 200'
    subprocess.call(command, shell=True)

#run main and exit without fault
if __name__ == '__main__':
    main()
    exit(0)
