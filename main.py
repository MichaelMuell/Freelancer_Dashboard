#Search Input Data
import pandas as pd
import scrape_indeed
import requests
import scrape_gulp
import openpyxl as pxl

#daily_search = input("Do you want to start the daily search queries or use custom query? daily/custom ")
#print(daily_search)
    #else:
    #    key_words  = input("Enter the key word you are searching for: ")
    #    location = input("Enter the location of your dream job: ")
    #    sort = input("Enter the sort mechanism for the results (date/relevance): ")
    #    pages = int(input("Enter the number of pages you would like to scrape: " ))

queries = []

query1 = ['gi','Data Analytics','Remote','date','contract', 1]
query2 = ['gi','SQL','Remote','date','contract',1]
query3 = ['gi','Power BI', 'Remote', 'date','contract',1]
query4 = ['gi','Business Intelligence', 'Remote', 'date','contract',1]

queries.append(query1)
queries.append(query2)
queries.append(query3)
queries.append(query4)

data_indeed = pd.DataFrame()
data_gulp = pd.DataFrame()

for query in queries:

    platforms = query[0]
    key_words = query[1]
    location = query[2]
    sort = query[3]
    job_type = query[4]
    pages = query[5]

    if 'gi' in platforms:
        data_gulp = data_gulp.append(scrape_gulp.get_data(key_words,sort,pages))

    if 'gi' in platforms:
        data_indeed = data_indeed.append(scrape_indeed.get_data(key_words,location,sort,job_type,pages))

    print(data_gulp)
    print(data_indeed)

path = r'G:/My Drive/freelancer_jobs.xlsx'
writer = pd.ExcelWriter(path,engine='xlsxwriter')

if 'g' in platforms:
    data_gulp.to_excel(writer, sheet_name='gulp', header=True,index=False)

if 'i' in platforms:
    data_indeed.to_excel(writer, sheet_name='indeed', header=True,index=False)

writer.save()

#data_indeed.to_excel(f'C:/Users/Michael/Desktop/freelancer_jobs.xlsx', sheet_name='indeed', header=True,index=False)
#data_gulp.to_excel(f'C:/Users/Michael/Desktop/freelancer_jobs.xlsx', sheet_name='gulp', header=True,index=False)
