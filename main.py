#Search Input Data
import pandas as pd
import scrape_indeed
import requests
import scrape_gulp

key_words  = input("Enter the key word you are searching for: ")
location = input("Enter the location of your dream job: ")
sort = input("Enter the sort mechanism for the results (date/relevance): ")
pages = int(input("Enter the number of pages you would like to scrape: " ))

data_indeed = pd.DataFrame()
data_gulp = pd.DataFrame()

data_gulp = scrape_gulp.get_data(key_words,location,sort,pages)
data_indeed = scrape_indeed.get_data(key_words,location,sort,pages)

data_indeed.to_csv(f'C:/Users/Michael/Desktop/indeed.csv', sep=',', header=True, mode='w+',index=False)
data_gulp.to_csv(f'C:/Users/Michael/Desktop/gulp.csv', sep=',', header=True, mode='w+',index=False)
