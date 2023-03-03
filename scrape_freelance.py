from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time

class freelance(): 
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
            self.sort = '2'
        else: self.sort == '1'

        page_counter = 1

        while page_counter <= self.pages:
            self.create_scrape_link(page_counter)
            self.get_page_data(self.scrape_link)

            page_counter+=1


    def get_page_data(self,link):

        freelance_html = requests.get(link).text
        soup =  BeautifulSoup(freelance_html,'lxml')
        jobs_list = soup.find('div',class_='project-list')
        jobs =  jobs_list.find_all('div',class_='list-item-main')

        job_list = []

        for job in jobs:

            job_title =  job.find('h3',class_='action-icons-overlap').text.strip()
            link = 'https://www.freelance.de'+job.find('a')['href']

            if job.find('ul',class_='tag-group margin-top-sm') is not None:
                job_skills =  job.find('ul',class_='tag-group margin-top-sm').text.strip()
            else: job_skills = 'empty'

            if job.find('i',class_='far fa-calendar-star fa-fw') is not None:
                start_date = job.find('i',class_='far fa-calendar-star fa-fw').next_sibling
            else: start_date = 'empty'

            if job.find('i',class_='far fa-map-marker-alt fa-fw') is not None:
                location = job.find('i',class_='far fa-map-marker-alt fa-fw').next_sibling
            else: location = 'empty'

            if job.find('i',class_='far fa-home-alt') is not None:
                remote = job.find('i',class_='far fa-home-alt').next_sibling
            else: remote = 'empty'

            if job.find('i',class_='far fa-history fa-fw') is not None:
                last_update = job.find('i',class_='far fa-history fa-fw').next_sibling
            else: last_update = 'empty'

            job_item = {
                'platform': 'freelance',
                'job_title': job_title,
                'job_skills': job_skills,
                'start_date': start_date,
                'location': location,
                'remote': remote,
                'last_update': last_update,
                'link': link
                }

            job_list.append(job_item)

        df =  pd.DataFrame(job_list)

        self.job_list = self.job_list.append(df)

    def translate_input(self):

        platforms,key_words,location,sort,job_type,pages = self



        return key_words,location,sort,pages

    def create_scrape_link(self,page_counter):

        url_base = 'https://www.freelance.de/search/project.php?'
        freetext_base = '__search_freetext='
    #    location_base = '__search_city='
        sort_base = '__search_sort_by='
        start_base = '_offset='
        jt_base= 'jt='

        freetext =  freetext_base+self.key_words.replace(' ','+')
    #    location = location_base+location
        sort = sort_base + self.sort
        start = start_base + str((self.pages - 1) * 20)

        self.scrape_link = (url_base+sort+'&'+freetext+'&'+self.location+'&'+start)
