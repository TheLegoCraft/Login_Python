
"""Login test"""

from pathlib import Path

def checkFileExists():
    file = Path("login_save.txt")
    return file.exists()

def savePassword(password):
    file = open("login_save.txt" , mode="w")
    file.write(password)
    file.close() 

def readPassword():
    file = open("login_save.txt" , mode="r")
    password = file.read()
    file.close()
    return password

def checkPassword(password):
    SAVED_PASSWORD = readPassword()

    if password==SAVED_PASSWORD:
        return True
    else:
        return False

if checkFileExists():

    print("Enter you password")
    USER_PASSWORD = raw_input()
    if checkPassword(USER_PASSWORD):
        print('You are logged in')
    else:
        print('Your password is not correct')

else:
    print("Enter the Password to save")
    USER_PASSWORD = raw_input()

    savePassword(USER_PASSWORD)





