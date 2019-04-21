class ProductPackaging(object):

    def __init__(self, packaging, packaging_tags, emb_codes, emb_codes_tags, first_packaging_code_geo):
        self.Packaging = packaging
        self.PackagingTags = packaging_tags
        self.EmbCodes = emb_codes
        self.EmbCodesTags = emb_codes_tags
        self.FirstPackagingCodeGeo = first_packaging_code_geo

    def __str__(self):
        return "Packaging => {0} # packaging_tags => {1}".format(self.Packaging, self.PackagingTags)
