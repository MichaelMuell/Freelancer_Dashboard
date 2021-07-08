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

    job_title_rows = []
    company_location_rows = []
    company_name_rows = []
    company_rating_rows = []
    job_snippet_rows = []
    posted_rows = []
    salary_snippet_rows = []
    link_rows = []

    for job in jobs:
        job_title = job.find('span', class_=lambda x: x != 'label').text
        job_title_rows.append(job_title)

        company_location = job.find('div', class_='companyLocation').text
        company_location_rows.append(company_location)

        company_name = job.find('span', class_='companyName').text
        company_name_rows.append(company_name)

        if job.find('span', class_='ratingNumber')is not None:
            company_rating = job.find('span', class_='ratingNumber').text
            company_rating_rows.append(company_rating)

        if job.find('div', class_='job-snippet')is not None:
            job_snippet = job.find('div', class_='job-snippet').text
            job_snippet_rows.append(job_snippet)

        if job.find('span', class_='date')is not None:
            posted = job.find('span', class_='date').text
            posted_rows.append(posted)

        if job.find('span', class_='salary-snippet')is not None:
            salary_snippet = job.find('span', class_='salary-snippet').text
            salary_snippet_rows.append(salary_snippet)

        link = job['href']
        link_rows.append(f'https://www.indeed.com'+ link)

        i+=1

    print(i)
    df = pd.DataFrame(list(zip(job_title_rows,\
                               company_location_rows,\
                               company_name_rows,\
                               company_rating_rows,\
                               job_snippet_rows,\
                               posted_rows)), \
                               columns =['job_title',\
                                         'company_location',\
                                         'company_name',\
                                         'company_rating',\
                                         'job_snippet',\
                                         'posted_rows'])

    df.to_csv(f'C:/Users/Michael/Desktop/filename.csv', sep=',', header=True, mode='w+')

    return i

input = 1
counter = 0
total_scrape_count = 0

while counter < input:
    indeed_html = requests.get(f'https://www.indeed.com/jobs?q=SQL&l=Remote&sort=date&start='+str(counter)+'&vjk=b7fcb744c2617103').text
    counter+=1
    result = getpage(indeed_html)
    total_scrape_count = total_scrape_count + result

print(total_scrape_count)
