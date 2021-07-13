from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib
from selenium import webdriver

scrape_link = 'https://www.gulp.de/gulp2/g/projekte?scope=projects&query=Data%20analytics&order=RELEVANCE_DESC'

driver = webdriver.Chrome()

driver.get(scrape_link)
soup = BeautifulSoup(driver.page_source, 'lxml')

driver.quit()

list_container = soup.find('ul',class_='ng-star-inserted')
jobs_list = list_container.find_all('div',class_='result-container')

job_list = []

for job in jobs_list:

    job_title = job.find('a').text

    if job.find('div',class_='flex start-date ng-star-inserted') is not None:
        start_date =  job.find('div',class_='flex start-date ng-star-inserted').text
    else: start_date = 'empty'

    if job.find('b') is not None:
        location =  job.find('b').text
    else: location = 'empty'

    job_info =  job.find('p', class_='description').text

    if job.find('div', class_='skills flex ng-star-inserted') is not None:
        job_skills =  job.find('div', class_='skills flex ng-star-inserted').text
    else: job_skills = 'empty'

    job_posted = job.find('span', class_='has-tip margin-top-1 time-ago').text

    link =  'https://www.gulp.de/' + job.find('a')['href']

    job_item = {
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

print(df)
#for jobs in jobs_list:
#    print(jobs.prettify())

#print(soup.prettify())