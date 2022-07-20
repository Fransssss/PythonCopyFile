# file copy
# Author : Fransiskus Agapa
import shutil

print("\n== File Copy ==")
print("1. Display file")
print("2. Copy file to project folder")
print("3. Copy file to a directoy")
print("E. Exit ")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Display file ]")
        try:
            with open("ThisFile.txt") as file:
                print(file.read())
        except FileNotFoundError:
            print("File is not found")
    elif choice == '2':
        print("\n[ Copy file to project folder ]")
        change_file_name = input("Would you like to change file name: ")
        if change_file_name == 'y' or change_file_name == 'Y':
            rename_file = input("Input file name: ")
            rename_file += ".txt"
            shutil.copyfile("ThisFile.txt", rename_file)
            print("[ File copied ]")
        elif change_file_name == 'n' or change_file_name == 'N':
            shutil.copyfile("ThisFile.txt", "CopiedFile.txt")
            print("[ File copied ]")
        else:
            print("[ Invalid input ]")
    elif choice == '3':
        print("\n[ Copy file to a directory ]")
        change_file_name = input("would you like to rename the copy file (y/n): ")
        if change_file_name == 'y' or change_file_name == 'Y':
            rename_file = input("input file name: ")
            rename_file += ".txt"
            shutil.copyfile("ThisFile.txt", r"C:\Users\XaveF\Documents" + '\\' + rename_file)
            print("[ File copied and renamed in a directory ]")
        elif change_file_name == 'n' or change_file_name == 'N':
            shutil.copyfile("ThisFile.txt", "CopiedFile.txt")
            print("[ File copied into a directory ]")
        else:
            print("[ Invalid input ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== File Copy ==")
    print("1. Display file")
    print("2. Copy file to project folder")
    print("3. Copy file to a directoy")
    print("E. Exit ")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")
