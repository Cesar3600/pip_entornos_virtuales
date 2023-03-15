
import matplotlib.pyplot as plt
import csv

def show_data(path,name_country,f):
    with open(path,'r') as filecsv:
        fileReader = csv.reader(filecsv,delimiter=',')
        header = next(fileReader)
        list_countries = []
        for country in fileReader:
            country_data = zip(header,country)
            country_dict = {key:value for key,value in country_data}
            list_countries.append(country_dict)

        info_country= list(filter(lambda country: country['Country/Territory'] == name_country,  list_countries ))

        x = {key:value for key,value in info_country[0].items() if key == f[0] or key == f[1] or key == f[2] or key == f[3] or key == f[4] or key == f[5] or key ==f[6]}

        return x


    
fields = ('2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population')
path = './app/data.csv'
country_name = 'Peru'

result = show_data(path,country_name,fields)

print(result)















































'''
import csv


def reform_data(path_csv,name):
    with open(path_csv,'r') as fileCsv:
        readerCsv = csv.reader(fileCsv,delimiter=',')
        list_countries=[]
        header = next(readerCsv)
        for body in readerCsv:
            countries_data = zip(header,body)
            country_dict= {key:value for key,value in countries_data}
            list_countries.append(country_dict)

        return list(filter( lambda country: country['Country/Territory']==name, list_countries))


path = './app/data.csv'
name='Peru'
result = reform_data(path,name)

print(result)

'''

