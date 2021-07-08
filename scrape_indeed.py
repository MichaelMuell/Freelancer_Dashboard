from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib

indeed_html = requests.get('https://www.indeed.com/jobs?q=SQL&l=Remote&sort=date&vjk=1d8515cad94915e9').text
soup = BeautifulSoup(indeed_html, 'lxml')

jobs_list = soup.find('div', id = 'mosaic-provider-jobcards')
jobs = jobs_list.find_all('div', class_ = 'slider_container')

i = 0

for job in jobs:
    job_title = job.find('span', class_=lambda x: x != 'label').text
    print(job_title)

    company_location = job.find('div', class_='companyLocation').text
    print(company_location)

    company_name = job.find('span', class_='companyName').text
    print(company_name)

    if job.find('span', class_='ratingNumber')is not None:
        company_rating = job.find('span', class_='ratingNumber').text
        print(company_rating)

    if job.find('div', class_='job-snippet')is not None:
        job_snippet = job.find('div', class_='job-snippet').text
        print(job_snippet)

    if job.find('span', class_='date')is not None:
        posted = job.find('span', class_='date').text
        print(posted)

    print('____________________________________')
    i = i+1

print(i)





#job_title_new = job.find('h2', class_ = 'jobTitle jobTitle-color-purple jobTitle-newJob')
#job_title_old = job.find('h2', class_ = 'jobTitle jobTitle-color-purple jobTitle')
