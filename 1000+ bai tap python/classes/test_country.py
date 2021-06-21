from . import country

australia = country.Country('Australia', 23545500, 7692024)
andorra = country.Country('Andorra', 76098, 468)
brazil = country.Country('Brazil', 202794000, 8515767)
china = country.Country('China', 1393000000, 9597000)
madagascar = country.Country('Madagascar', 26260000, 587000)

def test_country():

    assert (australia.is_big, True)
    assert (australia.compare_pd(andorra) == 'Australia has a smaller population density than Andorra')

    assert (andorra.is_big, False)
    assert (andorra.compare_pd(australia) == 'Andorra has a larger population density than Australia')

    assert (brazil.is_big, True)
    assert (brazil.compare_pd(china) == 'Brazil has a smaller population density than China')

    assert (china.is_big, True)
    assert (china.compare_pd(madagascar) == 'China has a larger population density than Madagascar')

    assert (madagascar.is_big, False)
    assert (madagascar.compare_pd(australia) == 'Madagascar has a larger population density than Australia')

