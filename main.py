#!/usr/bin/python

import os, sys
from menu import *
from singlehost import *
from maccapture import *

banner = """

===============================================
      __   ___   ___
_____/ _\_/  _\_/  _\_______
 ___/ /__/  /__/  /_____________
   |/ \___/ \___/ \ \_________________
                   \___CALABAR TOOLKIT
                                  v1.0

author: @nahberry
===============================================

"""

unsuportedItem = """

This feature has not been built yet...

):

"""

# Function for returning back to the main menu after running a script

def returnToMenu():
    print("  ")
    menuReturn = input("calabar > Run another scan? (y/n):" )
    while menuReturn != "null":
        if menuReturn == "y":
            break
            scanningMenu()
        elif menuReturn == "n":
            os.system("main.py")
            break
        else:
            print("Not a valid option. Try again.")
            returnToMenu()

# Function for returning to main menu if an unsupported selection was made
# This will be removed once all scripts have been loaded

def unsupportedReturn():
    returning = input("calabar > Press Enter to return to menu!")
    if returning != "null":
        os.system("main.py")

def main():

    print(banner)
    mainMenu()

    mainSelection = 6

    while mainSelection != 0:
        mainSelection = int(input("calabar > "))

        if mainSelection == 1:
            scanningMenu()
            scanMenuSelection = int(input("calabar > "))

            while scanMenuSelection != 0:

                if scanMenuSelection == 1:
                    singleHostScan()
                    returnToMenu()
                elif scanMenuSelection == 2:
                    captureMac()
                    returnToMenu()

        elif mainSelection == 2:
            print(unsuportedItem) # Remove after this has been built
            unsupportedReturn()

        elif mainSelection == 3:
            print(unsuportedItem) # Remove after this has been built
            unsupportedReturn()

        elif mainSelection == 4:
            print(unsuportedItem) # Remove after this has been built
            unsupportedReturn()

        elif mainSelection == 5:
            exit()

        else:
            print("calabar > Invalid option...")
            mainMenu()

main()
