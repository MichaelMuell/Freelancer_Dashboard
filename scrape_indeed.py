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

    job_list = []

    for job in jobs:
        if job.find('span', class_=lambda x: x != 'label')is not None:
            job_title = job.find('span', class_=lambda x: x != 'label').text
        else: job_title = 'empty'

        if job.find('div', class_='companyLocation')is not None:
            company_location = job.find('div', class_='companyLocation').text
        else: company_location = 'empty'

        if job.find('span', class_='companyName')is not None:
            company_name = job.find('span', class_='companyName').text
        else: company_name = 'empty'

        if job.find('span', class_='ratingNumber')is not None:
            company_rating = job.find('span', class_='ratingNumber').text
        else: company_rating = 'empty'

        if job.find('div', class_='job-snippet')is not None:
            job_snippet = job.find('div', class_='job-snippet').text
        else:
            job_snippet = 'empty'

        if job.find('span', class_='date')is not None:
            posted = job.find('span', class_='date').text
        else:
            posted = 'empty'

        if job.find('span', class_='salary-snippet')is not None:
            salary_snippet = job.find('span', class_='salary-snippet').text
        else:
            salary_snippet = 'empty'

        if job['href'] is not None:
            link = 'https://www.indeed.com'+job['href']
        else: link = 'empty'

        job_item = {
        'job_title': job_title,
        'company_location': company_location,
        'company_name': company_name,
        'company_rating': company_rating,
        'job_snippet': job_snippet,
        'posted': posted,
        'salary_snippet': salary_snippet,
        'link': link
        }
        job_list.append(job_item)

        i+=1

    print(i)

    df = pd.DataFrame(job_list)
    return df

def create_scrape_link(key_words,location,sort,page):

    url_base = 'https://www.indeed.com/jobs?'
    q_base = 'q='
    l_base = 'l='
    sort_base = 'sort='
    start_base = 'start='

    q = (q_base+key_words.replace(' ', '+'))
    l = (l_base+location.replace(' ','+'))
    sort = (sort_base+sort)
    start = (start_base+str(page))

    link_to_scrape = (url_base+q+'&'+l+'&'+sort+'&'+start)
    return link_to_scrape
    print(link_to_scrape)
