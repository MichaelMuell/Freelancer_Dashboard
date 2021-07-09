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
            link = job['href']
        else: link = 'empty'

        job_title_rows.append(job_title)
        company_location_rows.append(company_location)
        company_name_rows.append(company_name)
        company_rating_rows.append(company_rating)
        job_snippet_rows.append(job_snippet)
        salary_snippet_rows.append(salary_snippet)
        posted_rows.append(posted)
        link_rows.append(f'https://www.indeed.com'+ link)

        i+=1

    print(i)
    for jobx in job_title_rows:
        print(jobx)

    df = pd.DataFrame(list(zip(job_title_rows,\
                               company_name_rows,\
                               company_location_rows,\
                               company_rating_rows,\
                               job_snippet_rows,\
                               salary_snippet_rows,\
                               posted_rows,\
                               link_rows)), \
                               columns =['job_title',\
                                         'company_name',\
                                         'company_location',\
                                         'company_rating',\
                                         'job_snippet',\
                                         'salary_snippet',\
                                         'posted_rows',
                                         'link_rows'])

    print(df)
    return df

input = 3
counter = 0
total_scrape_count = 0
scrape_data = pd.DataFrame()

while counter < input:
    indeed_html = requests.get(f'https://www.indeed.com/jobs?q=SQL&l=Remote&sort=date&start='+str(counter)+'&vjk=b7fcb744c2617103').text
    counter+=1
    data_page = getpage(indeed_html)
    print(data_page)
    scrape_data = scrape_data.append(data_page)
    print(scrape_data)

#    total_scrape_count = total_scrape_count + result
scrape_data.to_csv(f'C:/Users/Michael/Desktop/filename.csv', sep=',', header=True, mode='w+')
print(total_scrape_count)
