import pandas as pd
import openpyxl as pxl
from scrape_freelance import freelance
from scrape_gulp import gulp
from scrape_etengo import etengo
from scrape_indeed import indeed

class crawler():
    def __init__(self,queries):
        self.queries = queries

    def start(self):

        data = pd.DataFrame()

        for query in self.queries.values():
            
            print(query[1])

            g = gulp(query)
            g.get_data()

            f = freelance(query)
            f.get_data()

            t = etengo(query)
            t.get_data()

#            i = indeed(query)
#            i.get_data()

            data = pd.concat([data,f.job_list,g.job_list,t.job_list])
           
        data.drop_duplicates(subset=['job_title'], inplace=True, keep='first')

        path = r'G:/My Drive/Freelancer Dashboard/freelancer_jobs.xlsx'

        data.to_excel(path)


queries = {
           1:['','Data Analytics','Remote','date','contract', 1],
           2:['','SQL','Remote','date','contract',1],
           3:['','Power BI', 'Remote', 'date','contract',1],
           4:['','Business Intelligence', 'Remote', 'date','contract',1],
           5:['','Business Analyst', 'Remote', 'date','contract',1],
           6:['','Analytics Engineer', 'Remote', 'date','contract',1],
           7:['','Analyst', 'Remote', 'date','contract',1],
           8:['','Solution Architect', 'Remote', 'date','contract',1],
           9:['','Requirements Engineer', 'Remote', 'date','contract',1],
           10:['','BI Analyst', 'Remote', 'date','contract',1],
           11:['','Fabric', 'Remote', 'date','contract',1],
           12:['','Analytics Consultant', 'Remote', 'date','contract',1],
           13:['','BI Developer', 'Remote', 'date','contract',1],
           14:['','Azure', 'Remote', 'date','contract',1],
           15:['','SQL Server', 'Remote', 'date','contract',1],
           16:['','Data Warehouse', 'Remote', 'date','contract',1],
           17:['','DWH', 'Remote', 'date','contract',1],
           18:['','Data Engineer', 'Remote', 'date','contract',1]
        }

print(queries)

crawl = crawler(queries)

crawl.start()
