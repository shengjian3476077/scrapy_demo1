# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy_demo1.items import ScrapyDemo1Item

class ScrapyDemo1Pipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', host='localhost',db='bigdata',
                user='root', passwd='123', cursorclass = MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        query.addBoth(lambda _: item)
        return query

    def _conditional_insert(self, tx, item):
        #for download_url in item['download_url']:
        #    tx.execute("insert into dytt values(%s,%s,%s,%s)",(item['movie_name'],item['movie_url'],download_url,item['IMDb']))
        tx.execute("insert into dytt values(%s,%s,%s,%s)",(item['movie_name'],item['movie_url'],item['download_url'][0],item['IMDb']))
        #    log.msg("Item stored in db: %s" % item, level=log.DEBUG)
    #    dbpool.commit()

    def handle_error(self, e):
        log.err(e)
