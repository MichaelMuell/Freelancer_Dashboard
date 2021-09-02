#Search Input Data
import pandas as pd
import scrape_indeed
import requests
import scrape_gulp
import openpyxl as pxl
import scrape_freelance

#daily_search = input("Do you want to start the daily search queries or use custom query? daily/custom ")
#print(daily_search)
    #else:
    #    key_words  = input("Enter the key word you are searching for: ")
    #    location = input("Enter the location of your dream job: ")
    #    sort = input("Enter the sort mechanism for the results (date/relevance): ")
    #    pages = int(input("Enter the number of pages you would like to scrape: " ))

#ttest

queries = []

query1 = ['gif','Data Analytics','Remote','date','contract', 1]
query2 = ['gif','SQL','Remote','date','contract',1]
query3 = ['gif','Power BI', 'Remote', 'date','contract',1]
query4 = ['gif','Business Intelligence', 'Remote', 'date','contract',1]
query5 = ['gif','DWH BI', 'Remote', 'date','contract',1]

queries.append(query1)
queries.append(query2)
queries.append(query3)
queries.append(query4)
queries.append(query5)

data_indeed = pd.DataFrame()
data_gulp = pd.DataFrame()
data_freelance = pd.DataFrame()

for query in queries:

    platforms = query[0]
    key_words = query[1]
    location = query[2]
    sort = query[3]
    job_type = query[4]
    pages = query[5]

    if 'g' in platforms:
        data_gulp = data_gulp.append(scrape_gulp.get_data(key_words,sort,pages))

    if 'i' in platforms:
        data_indeed = data_indeed.append(scrape_indeed.get_data(key_words,location,sort,job_type,pages))

    if 'f' in platforms:
        data_freelance = data_freelance.append(scrape_freelance.get_data(key_words,location,sort,pages))

    print(data_gulp)
    print(data_indeed)
    print(data_freelance)

path = r'G:/My Drive/freelancer_jobs.xlsx'

workbook = pxl.load_workbook(path)

try:
    del workbook['freelance']
except Exception:
    pass

try:
    del workbook['gulp']
except Exception:
    pass

try:
    del workbook['indeed']
except Exception:
    pass

workbook.save(path)

with pd.ExcelWriter(path,engine='openpyxl',if_sheet_exist='replace') as writer:

    writer.book = pxl.load_workbook(path)

    data_gulp.to_excel(writer, sheet_name='gulp', header=True,index=False)
    data_indeed.to_excel(writer, sheet_name='indeed', header=True,index=False)
    data_freelance.to_excel(writer, sheet_name='freelance', header=True,index=False)

writer.save()

#data_indeed.to_excel(f'C:/Users/Michael/Desktop/freelancer_jobs.xlsx', sheet_name='indeed', header=True,index=False)
#data_gulp.to_excel(f'C:/Users/Michael/Desktop/freelancer_jobs.xlsx', sheet_name='gulp', header=True,index=False)
