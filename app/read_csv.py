
import csv

def read_csv(csv_path):
    with open(csv_path,'r') as CSV_file:
        CSV_reader = csv.reader(CSV_file,delimiter=',')
        header = next(CSV_reader)
        data =[]
        for row in CSV_reader:
            iterable = zip(header,row)
            country_dict = {key:value for key,value in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    data = read_csv('./app/data.csv')
   # print(data[0])
