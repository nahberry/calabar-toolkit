#!/usr/bin/python

import os, sys
from menu import *
from singlehost import *
from maccapture import *
import requests

url = input("Enter a site url: ")
res = requests.get(url)

print(res.text)
print(res.status_code)
