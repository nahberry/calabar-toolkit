#!/usr/bin/python

import os, sys
from menu import *
from singlehost import *
from maccapture import *
import requests
from bs4 import BeautifulSoup

#Input URL for scraping
url = input("Enter a site url: ")
#Create requests to get site contents
page = requests.get(url)

#Store contents in a variable
txt = page.text
status = page.status_code

#Parse HTML with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#Extract title of page
pageTitle = soup.title.text
pageBody = soup.body
pageHead = soup.head

#Create lists for content
all_h1_tags = []
all_p_tags = []
image_data = []
all_links = []
top_items = []

#Set list to all H1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

#Set list to all P tags of the soup
for element in soup.select('P'):
    all_p_tags.append(element.text)


#Extract images and store them in the image_data list
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})


#Extract and store links in the all_links list
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

#Extract and store data in top_items

products = soup.select('div.thumbnail')
for elm in products:
    title = elm.select('h4 > a.title')[0].text
    reviewLabel = elm.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": reviewLabel.strip()
    }

    top_items.append(info)
