#Search Input Data
import pandas as pd
import scrape_indeed
import requests
import scrape_gulp

key_words  = input("Enter the key word you are searching for: ")
location = input("Enter the location of your dream job: ")
sort = input("Enter the sort mechanism for the results (date/relevance): ")
pages = int(input("Enter the number of pages you would like to scrape: " ))

page_counter = 0

data_indeed = pd.DataFrame()
data_gulp = pd.DataFrame()

while page_counter < pages:

    scrape_link = scrape_indeed.create_scrape_link(key_words,location,sort,page_counter)
    print(scrape_link)

    indeed_html = requests.get(scrape_link).text

    page_data_indeed = scrape_indeed.getpage(indeed_html)
    data_indeed = data_indeed.append(page_data_indeed)

    scrape_link = scrape_gulp.create_scrape_link(key_words,sort,page_counter+1)
    print(scrape_link)

    page_data_gulp = scrape_gulp.getpage(scrape_link)
    data_gulp = data_gulp.append(page_data_gulp)

    page_counter+=1
    print(data_indeed)
    print(data_gulp)

data_indeed.to_csv(f'C:/Users/Michael/Desktop/indeed.csv', sep=',', header=True, mode='w+')

data_gulp.to_csv(f'C:/Users/Michael/Desktop/gulp.csv', sep=',', header=True, mode='w+')
