import pandas as pd
import openpyxl as pxl
from scrape_freelance import freelance
from scrape_gulp import gulp
from scrape_etengo import etengo

class crawler():
    def __init__(self,queries):
        self.queries = queries

    def start(self):

        data = pd.DataFrame()

        for query in self.queries.values():
            
            print(query[1])

            f = freelance(query)
            f.get_data()

            g = gulp(query)
            g.get_data()

            t = etengo(query)
            t.get_data()

            data = pd.concat([data,f.job_list,g.job_list,t.job_list])
           
        data.drop_duplicates(subset=['job_title'], inplace=True, keep='first')

        path = r'G:/My Drive/Freelancer Dashboard/freelancer_jobs.xlsx'

        data.to_excel(path)


queries = {
           1:['','Data Analytics','Remote','date','contract', 1],
           2:['','SQL','Remote','date','contract',1],
           3:['','Power BI', 'Remote', 'date','contract',1],
           4:['','Business Intelligence', 'Remote', 'date','contract',1],
           5:['','DWH BI', 'Remote', 'date','contract',1],
           6:['','Analytics Engineer', 'Remote', 'date','contract',1],
           7:['','Data Warehouse', 'Remote', 'date','contract',1],
           8:['','Data Engineer', 'Remote', 'date','contract',1]
        }

print(queries)

crawl = crawler(queries)

crawl.start()
