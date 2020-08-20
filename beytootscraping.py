#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:57:55 2019

@author: dariush
"""

# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk


# get full text of 1 article to test processing text and subject into dataframe

url = "https://www.beytoote.com/news/sporty-news/tnews11058901.html"


# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

# send request to download the data
page = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(page.text, 'html.parser')

article = data.find_all("article", {"class": "item-page"})


print(article)
