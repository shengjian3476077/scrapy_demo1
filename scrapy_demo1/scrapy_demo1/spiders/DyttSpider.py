#coding:utf-8

import scrapy
from scrapy_demo1.items import ScrapyDemo1Item
import urllib2
import re

num = 1
class DyttSpider(scrapy.Spider):
    name = 'DyttSpider'
    allowed_domains = ["ygdy8.net"]
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self,response):
        #print response+"11111111111"
        divs = response.xpath('//a[@class="ulink"]')
        for div in divs:
            item = ScrapyDemo1Item()
            movie_url = div.xpath('@href')[0].extract()
            movie_name = div.xpath('text()')[0].extract()
            item["movie_url"] = movie_url if "http:" in movie_url else ("http://www.ygdy8.net"+ movie_url)
            my_response = urllib2.urlopen(item["movie_url"])
            html = my_response.read()
            IMDb = re.findall("(...)/10 from",html,re.S)
            item["IMDb"] = IMDb[0] if len(IMDb) else ('')
            item["movie_name"] = movie_name
            yield scrapy.Request(url = item["movie_url"],meta = {"item":item},callback = self.parse_detail,dont_filter=False)
        global num
        num = num + 1
        if (num <= 5):
            next_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_" + str(num) + ".html"
            yield scrapy.Request(url = next_url,callback = self.parse,dont_filter=False)
        #item = ScrapyDemo1Item()


    def parse_detail(self,response):
        item = response.meta["item"]
        item["download_url"] = response.xpath('//tbody/tr/td/a/text()').extract()
        return item