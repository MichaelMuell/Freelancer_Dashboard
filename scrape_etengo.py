import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 
from webdriver_manager.chrome import ChromeDriverManager

class etengo():
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
        driver = webdriver.Chrome(ChromeDriverManager().install())


        driver.get("https://www.etengo.de/en/it-project-search/")
        driver.implicitly_wait(5)

        search_box = driver.find_element(By.CSS_SELECTOR,"input.formText.project-text-search")
        driver.execute_script("arguments[0].scrollIntoView();", search_box)
        driver.execute_script("arguments[0].click();", search_box)

        search_box.send_keys(self.key_words)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        projects = driver.find_elements(By.CLASS_NAME,"card-content")

        job_list = []

        for project in projects:
            
            project_parts = project.text.splitlines()

            project_number = project_parts[2].split('-')

            project_link = 'https://www.etengo.de/it-projektsuche/' + project_number[1]

            job_item = {
                                'platform': 'etengo',
                                'job_title': project_parts[0],
                                'start_date':project_parts[8],
                                'location': project_parts[4],
                                'job_info': project_parts[6],
                                'job_skills': project_parts[10],
                                'job_posted': '',
                                'link': project_link
                        }
            job_list.append(job_item)

        self.job_list = pd.concat([self.job_list,pd.DataFrame(job_list)])

