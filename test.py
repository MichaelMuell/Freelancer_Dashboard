from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import numpy as np
import time
import html5lib
import scrape_gulp
from selenium import webdriver

df = pd.DataFrame()

df = scrape_gulp.getpage_gulp()

print(df)

def test():
    print('test')
