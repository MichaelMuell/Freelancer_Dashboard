import pandas as pd
import scrape_indeed
import scrape_gulp
import openpyxl as pxl
import scrape_freelance

class crawler():
    def __init__(self,queries):
        self.queries = queries

    def start(self):
        data_indeed = pd.DataFrame()
        data_gulp = pd.DataFrame()
        data_freelance = pd.DataFrame()

        for query in self.queries.values():
        
            print(query)
            data_freelance = freelance.getdata(query)

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
