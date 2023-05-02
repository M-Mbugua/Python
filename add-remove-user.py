# Python 3.10.1
# Encoding UTF-8
# Sys Admin tasks: adding and removing users in a system

import os


# Adding a new user
def new_user():
    confirm = "N"

    while confirm != "Y":
        username = input("Enter the username you would like to use: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo useradd " + username)


# Driver code
new_user()


# Removing a user
def remove_user():
    confirm = "N"

    while confirm != "Y":
        username = input("Enter the username you would like to remove: ")
        print("Remove the user '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r" + username)

