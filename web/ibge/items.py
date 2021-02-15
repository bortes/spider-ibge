# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MunicipioItem(scrapy.Item):
    uf     = scrapy.Field()
    codigo = scrapy.Field()
    nome   = scrapy.Field()
    link   = scrapy.Field()
