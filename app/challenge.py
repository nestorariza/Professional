import utils
import read_csv
import chart


def run():
    data = read_csv.read_csv('./app/data.csv')
    # data = list(
    #     filter(lambda item: item['Continent'] == 'Asia', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(
        map(lambda x: float(x['World Population Percentage']), data))
    # chart.generate_pie_chart(countries, percentages)
    chart.generate_bar_chart(countries, percentages)

    # country = input('Type Country => ')
    # result = utils.population_by_country(data, country)
    # if len(result) > 0:
    #     country = result[0]
    #     labels, values = utils.get_population(country)
    #     chart.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()
