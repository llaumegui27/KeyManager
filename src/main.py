import os

def start():
    action = False 
    while action is False:
        usage = input("Do you want to open an existing secure vault ? [1] Or create a new secure vault ? [2] : ")
        if usage == "1":
            action = True
        elif usage == "2":
            action = True
    return usage

def encrypt_db():
    return false

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
            except FileExistsError:
                print("This file already exists")
        else:
            try:
                db = open("../" + filename, "x")
                created_db = True
            except FileExistsError:
                print("This file already exists")

def main():
    if start() == "1":
        print("Select your db file and enter you password")
    else:
        print("Let's create a new safe box")
        new_safebox()

if __name__ == "__main__":
    main()