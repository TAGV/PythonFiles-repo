# Login using the password module
## Run this file on terminal window

import getpass
import time

fhandle = open("/home/myubuntu/PycharmProjects/pythonProject/Test",'r')
set_passwd = input(f"Login to read contents of the file {fhandle.name}  : ")

no_attempts = 0
while no_attempts <= 3:
    check_passwd = getpass.getpass()            # Typed passwd is hidden from the end user
    if check_passwd == set_passwd:
        print("Logged in successfully!!!")
        print("Opening the file......")
        time.sleep(1)
        print(fhandle.read())
        break
    else:
        no_attempts += 1
        attempts_remaining = 3 - no_attempts
        if attempts_remaining == 0:
            print("You are account is Locked!!!Goodbye!!!")
            break
        print("Wrong password. Try Again!!!")
        print(f'No of attempts remaining : {attempts_remaining}')
        continue

print()
print("Now Closing the file......")
time.sleep(2)
fhandle.close()
print(fhandle.closed)
