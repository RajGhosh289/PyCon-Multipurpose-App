import weight_converter
import functions

print("""
         Welcome to PyCon App.
PyCon is programmed by author "Raj Ghosh"
          AUTHOR: "Raj Ghosh"
           DATE: 12-01-2020
      LICENSE: GNU PUBLIC LICENSE
             VERSION: 1.0

GITHUB: "https://github.com/RajGhosh289"
Type !help to print all available commands

    """)


while True:
    getI = input("PyCon ==> ")

    if getI.__contains__("!help"):
        print("!help - Print all available commands\n!quit - To terminate the program\n!newfile - To create a new file\n!editfile - To edit predefined file\n!wc - To open weight converter app\n")
    elif getI.__contains__("!newfile"):
        functions.creatNewFile(input("Enter a name for your file: "))
        print()
    elif getI.__contains__("!editfile"):
        functions.editFile(input("File name "), input("Edit: "))
        print()
    elif getI.__contains__("!wc"):
        weight_converter.calculator()
        print()
    elif getI.__contains__("!quit"):
        functions.quit()
    else:
        print("[Command >> " + getI + " <<]" + " is not recognised by our <system> -- type !help to print all available commands\n")

