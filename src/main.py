import os

from crypto import *

def start():
    action = False 
    while action is False:
        usage = input("Do you want to open an existing secure vault ? [1] Or create a new secure vault ? [2] : ")
        if usage == "1":
            action = True
        elif usage == "2":
            action = True
    return usage
    

def new_safebox():
    created_db = False
    while created_db is False:
        filename = input("Choose the name of your password database : ")
        filename = filename + ".kmdb"
        print(filename)

        db_location = input("Do you want to save the db file in a specific location [1] ? Or to save it at the root directory [2] : ")
        if db_location == "1":
            location = input("Choose the location of your password database : ")
            if location[-1] != "\\":
                location = location + "\\"
                location += filename
                print(location)
            else:
                location += filename
                print(location)
            try:
                db = open(location, "x")
                created_db = True
                password = password_declaration()
                encrypt_file(location, location, password)
            except FileExistsError:
                print("This file already exists \n Try again.")
        else:
            try:
                db = open("../" + filename, "x")
                created_db = True
                password = password_declaration()
                encrypt_file("../" + filename, "../" + filename, password)
            except FileExistsError:
                print("This file already exists \n Try again.")


def existing_safebox():
    selected_file = False
    while selected_file is False:
        db = input("Enter the location of your .kmdb file : ")
        if os.path.exists(db):
            password = input("Enter the password to unlock your password database : ")
            decrypt_file(db, db, password)
            selected_file = True
        else:
            print("This file does not exist")


def main():
    if start() == "1":
        print("Select your db file and enter you password")
        existing_safebox()
    else:
        print("Let's create a new safe box")
        new_safebox()

if __name__ == "__main__":
    main()