import scrapy
import logging
import operator

logging.getLogger('scrapy').setLevel(logging.WARNING)

class server_tracker(scrapy.Spider):
    name = 'DownDetector'
    start_urls = ['https://downdetector.com/status/escape-from-tarkov/']

    def parse (self, response):
        print (response.css('div.h2.entry-title.color-danger::text').extract())