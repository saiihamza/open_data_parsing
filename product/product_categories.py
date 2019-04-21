class ProductCategories(object):

    def __init__(self, categories, categories_tags, categories_fr):
        self.Categories = categories
        self.CategoriesTags = categories_tags
        self.CategoriesFr = categories_fr

    def __str__(self):
        return self.Categories
