
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  countryName = input('Tipea tu pais => ')

  country_info = utils.population_by_country(data,countryName)


  if len(country_info) > 0:
    country = country_info[0]
    labels,values = utils.get_population(country)
    charts.generate_bar_chart(countryName,labels, values)
    charts.generate_pie_chart(countryName,labels,values)


if __name__ == '__main__':
  run()
