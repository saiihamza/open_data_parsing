#!/usr/bin/env python
# encoding: utf-8
import datetime

import config
from product import *


class ProductsFactory:

    @staticmethod
    def __initialize__():
        config.ITEMS_COUNT = len(open(config.CSV_FILE_FULL_NAME).readlines()) - 1
        config.CURRENT_INDEX = 1
        config.INITIALIZED = True

    @staticmethod
    def __from_string_to_object(line):
        """
        Convertie une ligne de
        :param line:
        :return:
        """
        elements = line.split('\t')
        new_item = ProductEntity()
        new_item.Code = elements[0]
        new_item.ProductUrl = elements[1]
        new_item.Creator = elements[2]
        new_item.Created = datetime.fromtimestamp(int(elements[3]))
        new_item.Updated = datetime.fromtimestamp(int(elements[5]))
        new_item.ProductName = elements[7]
        new_item.GenericName = elements[8]
        new_item.Quantity = ProductQuantity(elements[9])
        new_item.Packaging = ProductPackaging(elements[10], elements[11], elements[24], elements[25], elements[26])
        new_item.Brands = ProductBrands(elements[12], elements[13])
        new_item.Categories = ProductCategories(elements[14], elements[15], elements[16])
        new_item.Origins = ProductOrigins(elements[17], elements[18])
        new_item.ManufacturingPlaces = ProductManufacturingPlaces(elements[19], elements[20])
        new_item.Labels = ProductLabels(elements[21], elements[22], elements[23])
        new_item.Cities = ProductCities(elements[27], elements[28])
        new_item.PurchasePlaces = elements[29]
        new_item.Stores = elements[30]
        new_item.Countries = ProductCountries(elements[31], elements[32], elements[33])
        new_item.Compositions = ProductCompositions()
        new_item.Compositions.IngredientsTextAllergens = elements[34]
        new_item.Compositions.AllergensFr = elements[35]
        new_item.Compositions.Traces = elements[36]
        new_item.Compositions.TracesTags = elements[37]
        new_item.Compositions.TracesFr = elements[38]
        new_item.Compositions.ServingSize = elements[39]
        new_item.Compositions.ServingQuantityNoNutriments = elements[40]
        new_item.Compositions.AdditivesN = elements[41]
        new_item.Compositions.Additives = elements[42]
        new_item.Compositions.AdditivesTags = elements[43]
        new_item.Compositions.AdditivesFr = elements[44]
        new_item.Compositions.IngredientsFromPalmOilN = elements[45]
        new_item.Compositions.IngredientsFromPalmOil = elements[46]
        new_item.Compositions.IngredientsFromPalmOilTags = elements[47]
        new_item.Compositions.IngredientsThatMayBeFromPalmOilN = elements[48]
        new_item.Compositions.IngredientsThatMayBeFromPalmOil = elements[49]
        new_item.Compositions.IngredientsThatMayBeFromPalmOilTags = elements[50]
        new_item.Compositions.NutritionGradeFr = elements[51]
        new_item.Compositions.NovaGroup = elements[52]
        new_item.Compositions.PnnsGroups1 = elements[53]
        new_item.Compositions.PnnsGroups2 = elements[54]
        new_item.States = ProductStates(elements[55], elements[56], elements[57])
        new_item.main_category = ProductMainCategorie(elements[59])
        return new_item

    @staticmethod
    def init_parameters():
        config.INITIALIZED = False

    @staticmethod
    def has_next():
        if not config.INITIALIZED:
            ProductsFactory.__initialize__()
        return config.CURRENT_INDEX < config.ITEMS_COUNT

    @staticmethod
    def get_next():
        if not config.INITIALIZED:
            ProductsFactory.__initialize__()

        with open(config.CSV_FILE_FULL_NAME) as csv:
            for i, l in enumerate(csv):
                if i == config.CURRENT_INDEX:
                    break
        config.CURRENT_INDEX += 1
        new_item = ProductsFactory.__from_string_to_object(l)
        return new_item


while ProductsFactory.has_next():
    next_item = ProductsFactory.get_next()
    print(next_item.main_category)
    #break

