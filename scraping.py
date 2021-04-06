#!/usr/bin/python

import os, sys
from menu import *
import requests
from bs4 import BeautifulSoup
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.table import Table

#Initiate rich console options
console = Console()

#Create lists for content
all_h1_tags = []
all_p_tags = []
image_data = []
top_items = []

#Set varuable for menu selection

def linkScraping():

    #Setup a menu
    print("")
    print("Enter a Site URL: ")
    url = input("calabar > ")

    #Assign site data to variable
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Setup rich table
    table = Table(show_header=True, header_style='bold #2070b2', title='SITE MAP')
    table.add_column('HREF', justify="left")
    table.add_column('TITLE', justify="center")

    all_links = []

    links = soup.select('a')
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": text})
        table.add_row(href, text)

    console.print(table)
