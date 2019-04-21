class ProductCountries(object):

    def __init__(self, countries, countries_tags, countries_fr):
        self.Countries = countries
        self.CountriesTags = countries_tags
        self.CountriesFr = countries_fr

    def __str__(self):
        return self.Countries
