import os

# First version
def deleteWithConfirmation(filename):
    try:
        if input("Delete " + filename + ", are you sure? Y/N") == "Y":
            os.unlink(filename)
    except FileNotFoundError:
        print("That file does not exist")


# deleteWithConfirmation("sample.log")


# Refactored version
def _deleteWithConfirmation(filename):
    try:
        if input("Delete " + filename + ", are you sure? Y/N") == "Y":
            os.unlink(filename)
    except FileNotFoundError:
        print("That file does not exist")


def handleErrorForDeleteWithConfirmation(filename):
    try:
        _deleteWithConfirmation(filename)
    except FileNotFoundError:
        print("That file does not exist")


handleErrorForDeleteWithConfirmation("sample.log")
