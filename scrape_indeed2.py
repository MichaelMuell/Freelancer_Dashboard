URL = "https://www.indeed.com/q-SQL-l-Remote-jobs.html"

import requests
import bs4
from bs4 import BeautifulSoup
import urllib
from urllib import urlopen

html = urllib.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")
len(soup)
