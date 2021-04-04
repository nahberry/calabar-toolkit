#!/usr/bin/python

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

def mainMenu():

    mainMenuOptions = """

    1. Scanning
    2. Crawling
    4. Sniffing
    5. Slither Away

    """
    print(mainMenuOptions)


def scanningMenu():

    scanMenu = """

    1. Single Host
    2. Device Capture (Captures a list of all available devices with their IP & MAC)

    """

    print(scanMenu)

def sniffingMenu():

    sniffMenuOptions = """

    1. Basic Packet Sniffing

    """
