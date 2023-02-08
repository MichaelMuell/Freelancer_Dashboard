import pandas as pd
import scrape_indeed
import scrape_gulp
import openpyxl as pxl
from scrape_freelance import freelance
from scrape_gulp import gulp

class crawler():
    def __init__(self,queries):
        self.queries = queries

    def start(self):
        data_indeed = pd.DataFrame()
        data_gulp = pd.DataFrame()
        data_freelance = pd.DataFrame()

        for query in self.queries.values():
        
            f = freelance(query)
            f.get_data()

            g = gulp(query)
            g.get_data()

            data_freelance = data_freelance.append(f.job_list)
            data_freelance.drop_duplicates(subset=['job_title'], inplace=True, keep='first')

            data_gulp = data_gulp.append(g.job_list)
            data_gulp.drop_duplicates(subset=['job_title'], inplace=True, keep='first')

#            if 'i' in platforms:
#                data_indeed = data_indeed.append(scrape_indeed.get_data(key_words,location,sort,job_type,pages))


        frames = [data_gulp,data_indeed,data_freelance]
        output = pd.concat(frames)

        path = r'G:/My Drive/Freelancer Dashboard/freelancer_jobs.xlsx'

        output.to_excel(path)


queries = {
           1:['','Data Analytics','Remote','date','contract', 1],
           2:['','SQL','Remote','date','contract',1],
           3:['','Power BI', 'Remote', 'date','contract',1],
           4:['','Business Intelligence', 'Remote', 'date','contract',1],
           5:['','DWH BI', 'Remote', 'date','contract',1],
           6:['','Analytics Engineer', 'Remote', 'date','contract',1],
           7:['','Data Warehouse', 'Remote', 'date','contract',1]
        }

print(queries)

test = crawler(queries)

test.start()
