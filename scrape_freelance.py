from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time

def get_data(inp_key_words,inp_location,inp_sort,inp_pages):

    key_words, location, sort, pages = translate_input(inp_key_words,inp_location,inp_sort,inp_pages)

    page_counter = 1
    data_freelance = pd.DataFrame()

    while page_counter <= pages:
        scrape_link = create_scrape_link(key_words,location,sort,page_counter)
        print(scrape_link)

        page_data_freelance = get_page_data(scrape_link)
        data_freelance = data_freelance.append(page_data_freelance)

        page_counter+=1

    return data_freelance

def get_page_data(link):

    freelance_html = requests.get(link).text
    soup =  BeautifulSoup(freelance_html,'lxml')
    jobs_list = soup.find('div',class_='project-list')
    jobs =  jobs_list.find_all('div',class_='list-item-main')

    job_list = []

    for job in jobs:

        job_title =  job.find('h3',class_='action-icons-overlap').text.lstrip()
        job_title.lstrip()
        link = 'https://www.freelance.de'+job.find('a')['href']

        if job.find('ul',class_='tag-group margin-top-sm') is not None:
            job_skills =  job.find('ul',class_='tag-group margin-top-sm').text
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
            }

        job_list.append(job_item)

    df =  pd.DataFrame(job_list)

    return(df)

def translate_input(key_words,location,sort,pages):

    if sort == 'date':
        sort = '2'
    else: sort == '1'

    return key_words,location,sort,pages

def create_scrape_link(key_words,location,sort,page):

    url_base = 'https://www.freelance.de/search/project.php?'
    freetext_base = '__search_freetext='
    location_base = '__search_city='
    sort_base = '__search_sort_by='
    start_base = '_offset='
    jt_base= 'jt='

    freetext =  freetext_base+key_words.replace(' ','+')
    location = location_base+location
    sort = sort_base + sort
    start = start_base + str((page - 1) * 20)

    scrape_link = (url_base+sort+'&'+freetext+'&'+location+'&'+start)

    return scrape_link
