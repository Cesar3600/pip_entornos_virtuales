
import utils
import read_csv
import charts
import pandas as pd

def run():

  df = pd.read_csv('data.csv')
  continentName= input('ingresar el Continente... ->')
  df = df[df['Continent'] == continentName]
#  print(df)
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(continentName,countries,percentages)

  data = read_csv.read_csv('./data.csv')
  countryName = input('Tipea tu pais => ')

  country_info = utils.population_by_country(data,countryName)

#  print(country_info)


  if len(country_info) > 0:
    country = country_info[0]
    labels,values = utils.get_population(country)
    charts.generate_bar_chart(countryName,labels,values)


if __name__ == '__main__':
  run()
