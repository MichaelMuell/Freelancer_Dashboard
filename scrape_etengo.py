from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()

driver.get("https://www.etengo.de/en/it-project-search/")
driver.implicitly_wait(10)

search_box = driver.find_element(By.CSS_SELECTOR,"input.formText.project-text-search")
driver.execute_script("arguments[0].scrollIntoView();", search_box)
driver.execute_script("arguments[0].click();", search_box)

search_box.send_keys("SQL")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

name = driver.find_elements(By.CLASS_NAME,"card-content")

text = name[0].text

print(text)





#".test_button4[value='Update']"

#form id="changepw_form" name="changepw" action="#" method="post">
#<div class="field3">
#<div class="field3">
#<div class="field3">
#<input class="test_button4" type="reset" value="Reset" style"font-size:21px"="">
#<input class="test_button4" type="submit" value="Update" style"font-size:21px"="">

#<input type="text" class="formText project-text-search" value="" placeholder="Please enter terms related to projects, activities or skills">



