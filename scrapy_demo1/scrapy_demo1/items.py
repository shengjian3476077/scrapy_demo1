# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import scrapy

class ScrapyDemo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = Field()
    movie_url = Field()
    download_url = Field()
    IMDb = Field()
    #pass
