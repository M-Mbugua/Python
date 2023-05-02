# Python3.6  
# Coding: utf-8 
# Program to run command line commands


import os
import subprocess


# Linux command to list files and folders in a particular directory
# os.system("ls")

# Linux command to list subprocesses in the long format
# subprocess.run(["ls","-l"])

# Linux command to long-list subprocesses in a specific directory
# subprocess.run(["ls","-l","README.md"])


# Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


# Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])