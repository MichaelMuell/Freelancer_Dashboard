import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 

class indeed():
    def __init__(self,query):
        self.platforms = query[0]
        self.key_words = query[1]
        self.location = query[2]
        self.sort = query[3]
        self.job_type = query[4]
        self.pages = query[5]
        self.job_list = pd.DataFrame()
        
    def get_data(self):

        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get("https://de.indeed.com/Jobs?q="+self.key_words+"&sc=0bf%3Aexrec(),kf%3Aattr(DSQF7)jt(parttime)%3B&fromage=7")
        driver.implicitly_wait(5)

#        search_box = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/div/div[1]/div/div[1]/div/div[2]/input")
#
#        driver.execute_script("arguments[0].click();", search_box)
#        search_box.send_keys(Keys.CONTROL + 'a')
#        search_box.send_keys(Keys.BACKSPACE)
#        time.sleep(2)
#        search_box.send_keys(self.key_words)
#        search_box.send_keys(Keys.ENTER)

#        time.sleep(2)

        projects = driver.find_elements(By.CLASS_NAME,"job_seen_beacon")

        job_list = []

        for project in projects:
            
            project_parts = project.text.splitlines()

#            project_number = project_parts[2].split('-')
            project_link =  project.find_element(By.TAG_NAME,"a").get_attribute('href')


            job_item = {
                                'platform': 'indeed',
                                'job_title': project_parts[0],
                                'start_date': '',
                                'location': '',
                                'job_info': '' ,
                                'job_skills': '',
                                'job_posted': '',
                                'link': project_link
                        }
            job_list.append(job_item)

        self.job_list = pd.concat([self.job_list,pd.DataFrame(job_list)])

