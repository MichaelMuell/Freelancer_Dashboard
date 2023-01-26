import pandas as pd
import scrape_indeed
import scrape_gulp
import openpyxl as pxl
from scrape_freelance import freelance

class crawler():
    def __init__(self,queries):
        self.queries = queries

    def start(self):
        data_indeed = pd.DataFrame()
        data_gulp = pd.DataFrame()

        for query in self.queries.values():
        
            print(query)

            f = freelance(query)
            f.get_data()

            if 'g' in platforms:
                data_gulp = data_gulp.append(scrape_gulp.get_data(key_words,sort,pages))

            if 'i' in platforms:
                data_indeed = data_indeed.append(scrape_indeed.get_data(key_words,location,sort,job_type,pages))

            print(data_gulp)
            print(data_indeed)

        frames = [data_gulp,data_indeed,f.job_list]
        output = pd.concat(frames)

        path = r'G:/My Drive/freelancer_jobs.xlsx'

        output.to_excel(path)


queries = {
           1:['f','Data Analytics','Remote','date','contract', 1],
           2:['f','SQL','Remote','date','contract',1],
           3:['f','Power BI', 'Remote', 'date','contract',1],
           4:['f','Business Intelligence', 'Remote', 'date','contract',1],
           5:['f','DWH BI', 'Remote', 'date','contract',1],
           6:['f','Analytics Engineer', 'Remote', 'date','contract',1],
           7:['f','Data Warehouse', 'Remote', 'date','contract',1]
        }

print(queries)

test = crawler(queries)

test.start()
