"""return a single string of the form City, Country. such as Santiago, Chile"""
def city_name(city, country, population=''):
    if population:
        full_name = f"{city}, {country} - population {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name # This line is outside the if/else block, so it runs no matter what.


