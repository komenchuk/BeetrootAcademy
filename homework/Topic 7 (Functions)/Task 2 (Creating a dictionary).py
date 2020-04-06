def make_country (name, capital):
    country = {}
    country['name'] = name
    country['capital'] = capital
    return country

dict_country = make_country(input('Country name: '), input('Capital name: '))
print(dict_country)