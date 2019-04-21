from datetime import datetime
from product.product_brands import ProductBrands
from product.product_categories import ProductCategories
from product.product_cities import ProductCities
from product.product_compositions import ProductCompositions
from product.product_countries import ProductCountries
from product.product_labels import ProductLabels
from product.product_manufacturing_places import ProductManufacturingPlaces
from product.product_origins import ProductOrigins
from product.product_packaging import ProductPackaging
from product.product_quantity import ProductQuantity
from product.product_states import ProductStates
from product.remote_product import RemoteProduct


class ProductEntity(RemoteProduct):

    def __init__(self):
        RemoteProduct.__init__(self)
        self.Code = ''
        self.Creator = ''
        self.Created = datetime()
        self.Updated = datetime()
        self.ProductName = ''
        self.GenericName = ''
        self.Quantity = ProductQuantity(None)
        self.Packaging = ProductPackaging(None, None, None, None, None)
        self.Brands = ProductBrands(None, None)
        self.Categories = ProductCategories(None, None, None)
        self.Origins = ProductOrigins(None, None)
        self.ManufacturingPlaces = ProductManufacturingPlaces(None, None)
        self.Labels = ProductLabels(None, None, None)
        self.Cities = ProductCities(None, None)
        self.PurchasePlaces = ''
        self.Stores = ''
        self.Countries = ProductCountries(None, None, None)
        self.Compositions = ProductCompositions()
        self.States = ProductStates(None, None, None)
        self.main_category = ''

    def __str__(self):
        return "Code {0} (voir {1}) créé le {2}".format(self.Code, self.ProductUrl, self.Updated)
