from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
from datetime import datetime

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

            if last_update != 'empty':
                try:
                    date_time_obj = datetime.strptime(last_update.strip(), '%d.%m.%Y %H:%M')
                    last_update = date_time_obj.strftime('%Y-%m-%d')
                except ValueError:
                    # Handle the case where date conversion fails
                    print(f"Could not convert {last_update} to date. Keeping original value.")


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

        self.job_list = pd.concat([self.job_list,pd.DataFrame(job_list)])

    def translate_input(self):

        platforms,key_words,location,sort,job_type,pages = self



        return key_words,location,sort,pages

    def create_scrape_link(self,page_counter):
        
        url_base = 'https://www.freelance.de/search/project.php?__search_sort_by=&__search_project_age=0&__search_profile_availability=0&__search_profile_update=0&__search_profile_apply_watchlist=0&__search_project_start_date=&__search_profile_ac=&__search_additional_filter=&__search=search&search_extended=0&__search_freetext=keyword&__search_city=&seal=e5f72fd9196318f738d5c8525638f71d6c773b2a&__search_city_location_id=&__search_city_country=&__search_city_country_extended=&search_id=d9ea1c890acb48599120d53a913b6cdf&search_simple=suchen&__search_country=&__search_hour_rate_modifier=&__search_hour_rate=&__search_experience_modifier=&__search_experience=&__search_additional_filter=&__search_project_age_remote=0&__search_project_start_date_remote=&__search_sort_by_remote=1'
    #    freetext_base = '__search_freetext='
    #    location_base = '__search_city='
    #    sort_base = '__search_sort_by='
    #    start_base = '_offset='
    #    jt_base= 'jt='

    #    freetext =  freetext_base+self.key_words.replace(' ','+')
    #    location = location_base+location
    #    sort = sort_base + self.sort
    #    start = start_base + str((self.pages - 1) * 20)

        self.scrape_link = (url_base.replace('keyword',self.key_words))
