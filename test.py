from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import numpy as np
import time
import html5lib

indeed_html = requests.get(f'https://www.indeed.com/jobs?q=SQL&l=Remote&sort=date&vjk=b7fcb744c2617103').text

soup = BeautifulSoup(indeed_html, 'lxml')

jobs_list = soup.find('div', id = 'mosaic-provider-jobcards')
jobs = jobs_list.find_all('a', class_='tapItem', href=True)

i = 0
job_title_rows = []
company_name_rows = []

for job in jobs:
    job_title = job.find('span', class_=lambda x: x != 'label').text
    job_title_rows.append(job_title)

    company_name = job.find('span', class_='companyName').text
    company_name_rows.append(company_name)

df = pd.DataFrame(list(zip(job_title_rows,company_name_rows)),columns =['job_title','company_name'])

df.to_csv(f'C:/Users/Michael/Desktop/filename.csv', sep=',', header=True)
