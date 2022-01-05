import scrapy


class BbcNewsSpider(scrapy.Spider):
    name = 'BBC_news'
    allowed_domains = ['bbc.co.uk']
    start_urls = ['http://bbc.co.uk/']

    def parse(self, response):
        pass
