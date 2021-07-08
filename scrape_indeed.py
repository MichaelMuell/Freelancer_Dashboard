from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib

def getpage(indeed_html):
    soup = BeautifulSoup(indeed_html, 'lxml')

    jobs_list = soup.find('div', id = 'mosaic-provider-jobcards')
    jobs = jobs_list.find_all('a', class_='tapItem', href=True)

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

        if job.find('span', class_='salary-snippet')is not None:
            salary_snippet = job.find('span', class_='salary-snippet').text
            print(salary_snippet)

        link = job['href']
        print(f'https://www.indeed.com'+ link)

        print('____________________________________')
        i+=1

    print(i)
    return i

input = 3
counter = 0
total_scrape_count = 0

while counter < input:
    indeed_html = requests.get(f'https://www.indeed.com/jobs?q=SQL&l=Remote&sort=date&start='+str(counter)+'&vjk=b7fcb744c2617103').text
    counter+=1
    result = getpage(indeed_html)
    total_scrape_count = total_scrape_count + result

print(total_scrape_count)

#job_title_new = job.find('h2', class_ = 'jobTitle jobTitle-color-purple jobTitle-newJob')
#job_title_old = job.find('h2', class_ = 'jobTitle jobTitle-color-purple jobTitle')
