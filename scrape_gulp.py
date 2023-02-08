from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib
from selenium import webdriver

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

        if self.sort == 'date':
            self.sort = 'DATE_DESC'
        else: 'RELEVANCE_DESC'

        page_counter = 1
        data_gulp = pd.DataFrame()

        while page_counter <= self.pages:

            self.create_scrape_link(page_counter)
            self.get_page_data()

            page_counter+=1


    def create_scrape_link(self,page_counter):

        url_base = 'https://www.gulp.de/gulp2/g/projekte?'
        q_base = 'query='
        sort_base = 'order='
        start_base = 'page='

        q = (q_base+self.key_words.replace(' ', '%20'))
        sort = (sort_base+self.sort)
        start = (start_base+str(self.pages))

        self.scrape_link = (url_base+q+'&'+start+'&'+sort)


    def get_page_data(self):

        driver = webdriver.Chrome()

        driver.get(self.scrape_link)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        driver.quit()
        list_container = soup.find('ul',class_='ng-star-inserted')
        jobs_list = list_container.find_all('div',class_='content-panel')

        job_list = []

        for job in jobs_list:

            job_title = job.find('a').text

            if job.find('div',class_='flex start-date ng-star-inserted') is not None:
                start_date =  job.find('div',class_='flex start-date ng-star-inserted').text
            else: start_date = 'empty'

            if job.find('b') is not None:
                location =  job.find('b').text
            else: location = 'empty'

            job_info =  " ".join(job.find('p', class_='description').text.split())

            if job.find('div', class_='skills flex ng-star-inserted') is not None:
                job_skills =  job.find('div', class_='skills flex ng-star-inserted').text
            else: job_skills = 'empty'

            job_posted = job.find('span', class_='has-tip margin-top-1 time-ago').text

            link =  'https://www.gulp.de' + job.find('a')['href']

            job_item = {
                    'platform': 'gulp',
                    'job_title': job_title,
                    'start_date': start_date,
                    'location': location,
                    'job_info': job_info,
                    'job_skills': job_skills,
                    'job_posted': job_posted,
                    'link': link
            }

            job_list.append(job_item)

        df =  pd.DataFrame(job_list)

        self.job_list = self.job_list.append(df)

