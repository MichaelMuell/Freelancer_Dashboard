#Search Input Data
import pandas as pd
import scrape_indeed
import requests

key_words  = input("Enter the key word you are searching for: ")
location = input("Enter the location of your dream job: ")
sort = input("Enter the sort mechanism for the results (date/relevance): ")
pages = int(input("Enter the number of pages you would like to scrape: " ))

page_counter = 0

scrape_data = pd.DataFrame()

while page_counter < pages:

    scrape_link = scrape_indeed.create_scrape_link_indeed(key_words,location,sort,page_counter)
    print(scrape_link)

    indeed_html = requests.get(scrape_link).text

    data_page = scrape_indeed.getpage_indeed(indeed_html)

    scrape_data = scrape_data.append(data_page)

    page_counter+=1
    print(scrape_data)

scrape_data.to_csv(f'C:/Users/Michael/Desktop/filename.csv', sep=',', header=True, mode='w+')
