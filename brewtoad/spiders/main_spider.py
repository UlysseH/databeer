import csv
import scrapy

# Import from brewtoad
from brewtoad.items import RecipeGeneralItem, StyleItem, FermentableItem, HopItem, YeastItem

class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["brewtoad.com"]
    start_urls = []

    def __init__(self, start='1', end='2'):
        self.start = int(start)
        self.end = int(end)
        for k in range(self.start, self.end):
            self.start_urls.append("https://www.brewtoad.com/recipes?page={}&sort=rank".format(k))
        # general
        fieldnames = [
            'beer_id',
            'beer_name',
            'mash_type',
            'brewer',
            'batch_size',
            'boil_size',
            'efficiency'
        ]
        self.csvfile_recipe = open('csv/recipes_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_recipe = csv.DictWriter(self.csvfile_recipe, fieldnames=fieldnames)
        self.writer_recipe.writeheader()
        # styles
        fieldnames = [
            'beer_id',
            'beer_name',
            'beer_style',
            'style_guide',
            'version',
            'style_letter',
            'category_number',
            'beer_type',
            'OG_min',
            'OG_max',
            'FG_min',
            'FG_max',
            'IBU_min',
            'IBU_max',
            'color_min',
            'color_max',
            'ABV_min',
            'ABV_max'
        ]
        self.csvfile_style = open('csv/styles_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_style = csv.DictWriter(self.csvfile_style, fieldnames=fieldnames)
        self.writer_style.writeheader()
        # fermentables
        fieldnames = [
            'beer_id',
            'beer_name',
            'name',
            'origin',
            '_type',
            '_yield',
            'amount',
            'potential',
            'color',
            'add_after_boil',
            'coarse_fine_diff',
            'moisture',
            'diastatic_power',
            'protein',
            'max_in_batch',
            'recommend_mash',
            'ibu_gal_per_lb',
            'notes'
        ]
        self.csvfile_fermentable = open('csv/fermentables_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_fermentable = csv.DictWriter(self.csvfile_fermentable, fieldnames=fieldnames)
        self.writer_fermentable.writeheader()
        # hops
        fieldnames = [
            'beer_id',
            'beer_name',
            'name',
            'origin',
            'alpha',
            'beta',
            'amount',
            'use',
            'form',
            'time',
            'notes'
        ]
        self.csvfile_hop = open('csv/hops_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_hop = csv.DictWriter(self.csvfile_hop, fieldnames=fieldnames)
        self.writer_hop.writeheader()
        # yeasts
        fieldnames = [
            'beer_id',
            'beer_name',
            'name',
            'laboratory',
            '_type',
            'form',
            'attenuation'
        ]
        self.csvfile_yeast = open('csv/yeasts_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_yeast = csv.DictWriter(self.csvfile_yeast, fieldnames=fieldnames)
        self.writer_yeast.writeheader()
        # miscs
        fieldnames = [
            'beer_id',
            'beer_name',
            'name',
            'use',
            'time',
            'amount',
            'amount_is_weight',
            'notes'
        ]
        self.csvfile_misc = open('csv/miscs_page_{0}_to_{1}.csv'.format(self.start, self.end), 'w+b')
        self.writer_misc = csv.DictWriter(self.csvfile_misc, fieldnames=fieldnames)
        self.writer_misc.writeheader()
        """
        self.recipes_file = open('csv/recipes_page_{0}_to_{1}.json'.format(self.start, self.end), 'w+b')
        self.styles_file = open('csv/styles_page_{0}_to_{1}.json'.format(self.start, self.end), 'w+b')
        self.fermentables_file = open('csv/fermentables_page_{0}_to_{1}.json'.format(self.start, self.end), 'w+b')
        self.hops_file = open('csv/hops_page_{0}_to_{1}.json'.format(self.start, self.end), 'w+b')
        self.yeasts_file = open('csv/yeasts_page_{0}_to_{1}.json'.format(self.start, self.end), 'w+b')
        """

    def parse(self, response):
        #import pdb; pdb.set_trace()
        for href in response.xpath('//a[@class="recipe-link"]/@href'):
            url = response.urljoin(href.extract()) + '.xml'
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        recipe_general = RecipeGeneralItem()
        style = StyleItem()
        fermentables = []
        hops = []
        yeasts = []
        # RecipeGeneralItem
        recipe_general['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
        recipe_general['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
        recipe_general['mash_type'] = response.xpath('//RECIPE/TYPE/text()').extract()
        recipe_general['brewer'] = response.xpath('//RECIPE/BREWER/text()').extract()
        recipe_general['batch_size'] = response.xpath('//RECIPE/BATCH_SIZE/text()').extract()
        recipe_general['boil_size'] = response.xpath('//RECIPE/BOIL_SIZE/text()').extract()
        recipe_general['efficiency'] = response.xpath('//RECIPE/EFFICIENCY/text()').extract()
        self.writer_recipe.writerow(recipe_general)

        # Style
        style['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
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
        self.writer_style.writerow(style)

        # Fermentables
        nb_of_fermentables = len(response.xpath('//FERMENTABLE'))
        for k in range(1, nb_of_fermentables):
            fermentable = FermentableItem()
            fermentable['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
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
            self.writer_fermentable.writerow(fermentable)

        # Hops
        nb_of_hops = len(response.xpath('//HOP'))
        for k in range(1, nb_of_hops):
            hop = HopItem()
            hop['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
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
            self.writer_hop.writerow(hop)

        # Yeasts
        nb_of_yeasts = len(response.xpath('//YEAST'))
        for k in range(1, nb_of_yeasts):
            yeast = YeastItem()
            yeast['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
            yeast['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            yeast['name'] = response.xpath('//YEAST[{}]/NAME/text()'.format(k)).extract()
            yeast['laboratory'] = response.xpath('//YEAST[{}]/LABORATORY/text()'.format(k)).extract()
            yeast['_type'] = response.xpath('//YEAST[{}]/TYPE/text()'.format(k)).extract()
            yeast['form'] = response.xpath('//YEAST[{}]/FORM/text()'.format(k)).extract()
            yeast['attenuation'] = response.xpath('//YEAST[{}]/ATTENUATION/text()'.format(k)).extract()
            self.writer_yeast.writerow(yeast)

        # Miscs
        nb_of_miscs = len(response.xpath('//YEAST'))
        for k in range(1, nb_of_miscs):
            misc = YeastItem()
            misc['beer_id'] = response.url.split('/')[-1].split('.xml')[0]
            misc['beer_name'] = response.xpath('//RECIPE/NAME/text()').extract()
            misc['name'] = response.xpath('//MISC[{}]/NAME/text()'.format(k)).extract()
            misc['use'] = response.xpath('//MISC[{}]/USE/text()'.format(k)).extract()
            misc['time'] = response.xpath('//MISC[{}]/TIME/text()'.format(k)).extract()
            misc['amount'] = response.xpath('//MISC[{}]/AMOUNT/text()'.format(k)).extract()
            misc['amount_is_weight'] = response.xpath('//MISC[{}]/AMOUNT_IS_WEIGHT/text()'.format(k)).extract()
            misc['notes'] = response.xpath('//MISC[{}]/NOTES/text()'.format(k)).extract()
            self.writer_misc.writerow(misc)

        yield 'ok'
