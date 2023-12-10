import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 
from webdriver_manager.chrome import ChromeDriverManager


class gulp():
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

        keyword_link = self.key_words.replace(' ', '%20')

        driver.get("https://www.gulp.de/gulp2/g/projekte?query="+keyword_link+"&page=1&order=DATE_DESC")
        driver.implicitly_wait(5)

        project_list = driver.find_element(By.XPATH,"//ul[contains(@class, 'ng-star-inserted')]")

        projects = project_list.find_elements(By.XPATH,"//div[contains(@class, 'content-panel margin-3')]")

        job_list = []

        for project in projects:
            
            project_title = project.find_element(By.TAG_NAME,"a").text
            details = project.find_element(By.CSS_SELECTOR,"ul.fa-ul").text.splitlines()

            project_location = ""  # Initialize to empty string
            project_start = ""

            for detail in details:
                if detail.find('Location') != -1: 
                    project_location = detail
                elif detail.find('Start') != -1: 
                    project_start = detail 
            
            project_link =  project.find_element(By.TAG_NAME,"a").get_attribute('href')
           
#            project_skills = project.find_element(By.CSS_SELECTOR,"span.label tertiary ng-star-inserted").text

            project_info = project.find_element(By.CSS_SELECTOR,"p.description").text

            project_posted = project.find_element(By.TAG_NAME,"small").text 

            if 'hour' in project_posted.lower():
                project_posted = 'hour'
            
            if 'minute' in project_posted.lower():
                project_posted = 'hour'

            job_item = {
                                'platform': 'gulp',
                                'job_title': project_title,
                                'start_date': project_start,
                                'location': project_location,
                                'job_info': project_info,
                                'job_skills': "",
                                'last_update': project_posted,
                                'link': project_link
                        }
            job_list.append(job_item)

        self.job_list = pd.concat([self.job_list,pd.DataFrame(job_list)])

