import scrapy

# Import from brewtoad
from brewtoad.items import RecipeGeneralItem, StyleItem, FermentableItem, HopItem, YeastItem

class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["brewtoad.com"]
    start_urls = []
    for k in range(1, 100):
        start_urls.append("https://www.brewtoad.com/recipes?page={}&sort=rank".format(k))

    def parse(self, response):
        for href in response.xpath('//a[@class="recipe-link"]/@href'):
            url = response.urljoin(href.extract()) + '.xml'
            print url
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        recipe_general = RecipeGeneralItem()
        style = StyleItem()
        fermentables = []
        hops = []
        yeasts = []

        # RecipeGeneralItem
        recipe_general['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
        recipe_general['mash_type'] = response.xpath('//RECIPE/TYPE/text()').extract()
        recipe_general['brewer'] = response.xpath('//RECIPE/BREWER/text()').extract()
        recipe_general['batch_size'] = response.xpath('//RECIPE/BATCH_SIZE/text()').extract()
        recipe_general['boil_size'] = response.xpath('//RECIPE/BOIL_SIZE/text()').extract()
        recipe_general['efficiency'] = response.xpath('//RECIPE/EFFICIENCY/text()').extract()
        #yield recipe_general

        # Style
        style['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
        style['beer_style'] = response.xpath('//STYLE//NAME/text()').extract()
        style['style_guide'] = response.xpath('//STYLE//STYLE_GUIDE/text()').extract()
        style['version'] = response.xpath('//STYLE//VERSION/text()').extract()
        style['style_letter'] = response.xpath('//STYLE//STYLE_LETTER/text()').extract()
        style['category_number'] = response.xpath('//STYLE//CATEGORY_NUMBER/text()').extract()
        style['beer_type'] = response.xpath('//STYLE//TYPE/text()').extract()
        style['OG_min'] = response.xpath('//STYLE//OG_MIN/text()').extract()
        style['OG_max'] = response.xpath('//STYLE//OG_MAX/text()').extract()
        style['FG_min'] = response.xpath('//STYLE//FG_MIN/text()').extract()
        style['FG_max'] = response.xpath('//STYLE//FG_MAX/text()').extract()
        style['IBU_min'] = response.xpath('//STYLE//IBU_MIN/text()').extract()
        style['IBU_max'] = response.xpath('//STYLE//IBU_MAX/text()').extract()
        style['color_min'] = response.xpath('//STYLE//COLOR_MIN/text()').extract()
        style['color_max'] = response.xpath('//STYLE//COLOR_MAX/text()').extract()
        style['ABV_min'] = response.xpath('//STYLE//ABV_MIN/text()').extract()
        style['ABV_max'] = response.xpath('//STYLE//ABV_MAX/text()').extract()
        #yield style

        # Fermentables
        nb_of_fermentables = len(response.xpath('//FERMENTABLE'))
        for k in range(1, nb_of_fermentables):
            fermentable = FermentableItem()
            fermentable['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            fermentable['name'] = response.xpath('//FERMENTABLE[{}]/NAME/text()'.format(k)).extract()
            fermentable['origin'] = response.xpath('//FERMENTABLE[{}]/ORIGIN/text()'.format(k)).extract()
            fermentable['_type'] = response.xpath('//FERMENTABLE[{}]/TYPE/text()'.format(k)).extract()
            fermentable['_yield'] = response.xpath('//FERMENTABLE[{}]/YIELD/text()'.format(k)).extract()
            fermentable['amount'] = response.xpath('//FERMENTABLE[{}]/AMOUNT/text()'.format(k)).extract()
            fermentable['potential'] = response.xpath('//FERMENTABLE[{}]/POTENTIAL/text()'.format(k)).extract()
            fermentable['color'] = response.xpath('//FERMENTABLE[{}]/COLOR/text()'.format(k)).extract()
            fermentable['add_after_boil'] = response.xpath('//FERMENTABLE[{}]/PROTEIN/text()'.format(k)).extract()
            fermentable['coarse_fine_diff'] = response.xpath('//FERMENTABLE[{}]/COARSE_FINE_DIFF/text()'.format(k)).extract()
            fermentable['moisture'] = response.xpath('//FERMENTABLE[{}]/MOISTURE/text()'.format(k)).extract()
            fermentable['diastatic_power'] = response.xpath('//FERMENTABLE[{}]/DIASTATIC_POWER/text()'.format(k)).extract()
            fermentable['protein'] = response.xpath('//FERMENTABLE[{}]/PROTEIN/text()'.format(k)).extract()
            fermentable['max_in_batch'] = response.xpath('//FERMENTABLE[{}]/MAX_IN_BATCH/text()'.format(k)).extract()
            fermentable['recommend_mash'] = response.xpath('//FERMENTABLE[{}]/RECOMMEND_MASH/text()'.format(k)).extract()
            fermentable['ibu_gal_per_lb'] = response.xpath('//FERMENTABLE[{}]/IBU_GAL_PER_LB/text()'.format(k)).extract()
            fermentable['notes'] = response.xpath('//FERMENTABLE[{}]/NOTES/text()'.format(k)).extract()
            #yield fermentable

        # Hops
        nb_of_hops = len(response.xpath('//HOP'))
        for k in range(1, nb_of_hops):
            hop = HopItem()
            hop['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            hop['name'] = response.xpath('//HOP[{}]/NAME/text()'.format(k)).extract()
            hop['origin'] = response.xpath('//HOP[{}]/ORIGIN/text()'.format(k)).extract()
            hop['alpha'] = response.xpath('//HOP[{}]/ALPHA/text()'.format(k)).extract()
            hop['beta'] = response.xpath('//HOP[{}]/BETA/text()'.format(k)).extract()
            hop['amount'] = response.xpath('//HOP[{}]/AMOUNT/text()'.format(k)).extract()
            hop['use'] = response.xpath('//HOP[{}]/USE/text()'.format(k)).extract()
            hop['form'] = response.xpath('//HOP[{}]/FORM/text()'.format(k)).extract()
            hop['time'] = response.xpath('//HOP[{}]/TIME/text()'.format(k)).extract()
            hop['notes'] = response.xpath('//HOP[{}]/NOTES/text()'.format(k)).extract()
            #yield hop

        # Yeasts
        nb_of_yeasts = len(response.xpath('//YEAST'))
        for k in range(1, nb_of_yeasts):
            yeast = YeastItem()
            yeast['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            yeast['name'] = response.xpath('//YEAST[{}]/NAME/text()'.format(k)).extract()
            yeast['laboratory'] = response.xpath('//YEAST[{}]/LABORATORY/text()'.format(k)).extract()
            yeast['_type'] = response.xpath('//YEAST[{}]/TYPE/text()'.format(k)).extract()
            yeast['form'] = response.xpath('//YEAST[{}]/FORM/text()'.format(k)).extract()
            yeast['attenuation'] = response.xpath('//YEAST[{}]/ATTENUATION/text()'.format(k)).extract()
            #yield yeast

        # Miscs
        nb_of_miscs = len(response.xpath('//YEAST'))
        for k in range(1, nb_of_miscs):
            misc = YeastItem()
            misc['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            misc['name'] = response.xpath('//MISC[{}]/NAME/text()'.format(k)).extract()
            misc['use'] = response.xpath('//MISC[{}]/USE/text()'.format(k)).extract()
            misc['time'] = response.xpath('//MISC[{}]/TIME/text()'.format(k)).extract()
            misc['amount'] = response.xpath('//MISC[{}]/AMOUNT/text()'.format(k)).extract()
            misc['amount_is_weight'] = response.xpath('//MISC[{}]/AMOUNT_IS_WEIGHT/text()'.format(k)).extract()
            misc['notes'] = response.xpath('//MISC[{}]/NOTES/text()'.format(k)).extract()
            #yield misc
