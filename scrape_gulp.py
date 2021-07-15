from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import html5lib
from selenium import webdriver

def get_data(inp_key_words, inp_sort, inp_pages):

    key_words, sort, pages = translate_input(inp_key_words,inp_sort,inp_pages)

    page_counter = 1
    data_gulp = pd.DataFrame()

    while page_counter <= pages:

        scrape_link = create_scrape_link(key_words,sort,page_counter)
        print(scrape_link)
        page_data_gulp = get_page_data(scrape_link)
        data_gulp = data_gulp.append(page_data_gulp)

        page_counter+=1

    return data_gulp

def translate_input(key_words, sort, pages):

    if sort == 'date':
        sort = 'DATE_DESC'
    else: 'RELEVANCE_DESC'

    return key_words,sort,pages

def create_scrape_link(key_words,sort,pages):

    url_base = 'https://www.gulp.de/gulp2/g/projekte?'
    q_base = 'query='
    sort_base = 'order='
    start_base = 'page='

    q = (q_base+key_words.replace(' ', '%20'))
    sort = (sort_base+sort)
    start = (start_base+str(pages))

    link_to_scrape = (url_base+q+'&'+start+'&'+sort)

    return link_to_scrape


def get_page_data(gulp_html):

    scrape_link = gulp_html

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

    return(df)

#get_data('SQL','Remote','date',2)
