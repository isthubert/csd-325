# Isaac St Hubert Module 7.2 11/22/2025
# This program describes a function that returns and prints city, country

def city_country(city, country, population=0, language=0):

    result = f"{city}, {country}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language}"

    return result

print(city_country("Santiago", "Chile"))
print(city_country("Orlando", "USA", 13000000))
print(city_country("Toronto", "Canada", 2000000, "English"))
