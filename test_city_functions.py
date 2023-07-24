from city_functions import city_name

def test_city_country():
    formatted_name = city_name('Santiago', 'Chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    formatted_name = city_name('Santiago', 'Chile', 5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'
    