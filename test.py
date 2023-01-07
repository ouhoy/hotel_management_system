from pycountry import countries

for country in list(countries):
    print(country.name)

morocco = countries.get(name="MoRocco")

print(morocco)
