# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrewtoadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class RecipeGeneralItem(scrapy.Item):
    beer_name = scrapy.Field()
    mash_type = scrapy.Field()
    brewer = scrapy.Field()
    batch_size = scrapy.Field()
    boil_size = scrapy.Field()
    efficiency = scrapy.Field()
    pass



class StyleItem(scrapy.Item):
    beer_name = scrapy.Field()
    beer_style = scrapy.Field()
    style_guide = scrapy.Field()
    version = scrapy.Field()
    style_letter = scrapy.Field()
    category_number = scrapy.Field()
    beer_type = scrapy.Field()
    OG_min = scrapy.Field()
    OG_max = scrapy.Field()
    FG_min = scrapy.Field()
    FG_max = scrapy.Field()
    IBU_min = scrapy.Field()
    IBU_max = scrapy.Field()
    color_min = scrapy.Field()
    color_max = scrapy.Field()
    ABV_min = scrapy.Field()
    ABV_max = scrapy.Field()



class FermentableItem(scrapy.Item):
    beer_name = scrapy.Field()
    name = scrapy.Field()
    origin = scrapy.Field()
    _type = scrapy.Field()
    _yield = scrapy.Field()
    amount = scrapy.Field()
    potential = scrapy.Field()
    color = scrapy.Field()
    add_after_boil = scrapy.Field()
    coarse_fine_diff = scrapy.Field()
    moisture = scrapy.Field()
    diastatic_power = scrapy.Field()
    protein = scrapy.Field()
    max_in_batch = scrapy.Field()
    recommend_mash = scrapy.Field()
    ibu_gal_per_lb = scrapy.Field()
    notes = scrapy.Field()
    pass



class HopItem(scrapy.Item):
    beer_name = scrapy.Field()
    name = scrapy.Field()
    origin = scrapy.Field()
    alpha = scrapy.Field()
    beta = scrapy.Field()
    amount = scrapy.Field()
    use = scrapy.Field()
    form = scrapy.Field()
    time = scrapy.Field()
    notes = scrapy.Field()
    pass



class YeastItem(scrapy.Item):
    beer_name = scrapy.Field()
    name = scrapy.Field()
    laboratory = scrapy.Field()
    _type = scrapy.Field()
    form = scrapy.Field()
    attenuation = scrapy.Field()
