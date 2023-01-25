import pandas as pd
import scrape_indeed
import scrape_gulp
import openpyxl as pxl
import scrape_freelance

queries = []

query1 = ['gif','Data Analytics','Remote','date','contract', 1]
query2 = ['gif','SQL','Remote','date','contract',1]
query3 = ['gif','Power BI', 'Remote', 'date','contract',1]
query4 = ['gif','Business Intelligence', 'Remote', 'date','contract',1]
query5 = ['gif','DWH BI', 'Remote', 'date','contract',1]
query6 = ['gif','Analytics Engineer', 'Remote', 'date','contract',1]
query7 = ['gif','Data Warehouse', 'Remote', 'date','contract',1]

queries.append(query1)
queries.append(query2)
queries.append(query3)
queries.append(query4)
queries.append(query5)

data_indeed = pd.DataFrame()
data_gulp = pd.DataFrame()
data_freelance = pd.DataFrame()

for query in queries:

    platforms,key_words,location,sort,job_type,pages = query

    if 'g' in platforms:
        data_gulp = data_gulp.append(scrape_gulp.get_data(key_words,sort,pages))

    if 'i' in platforms:
        data_indeed = data_indeed.append(scrape_indeed.get_data(key_words,location,sort,job_type,pages))

    if 'f' in platforms:
        data_freelance = data_freelance.append(scrape_freelance.get_data(key_words,location,sort,pages))

    print(data_gulp)
    print(data_indeed)
    print(data_freelance)

frames = [data_gulp,data_indeed,data_freelance]
output = pd.concat(frames)

path = r'G:/My Drive/freelancer_jobs.xlsx'

output.to_excel(path)