import scrapy
from scrapy import Spider, Request
from scrapy.settings.default_settings import DEFAULT_REQUEST_HEADERS
import re
from news_spider.items import NewsSpiderItem

import logging

logger = logging.getLogger()
level = logging.INFO
logger.setLevel(level)

hdlr = logging.FileHandler("./spider.log")
hdlr.setLevel(level)
logger.addHandler(hdlr)

logger1 = logging.getLogger()
level = logging.INFO
logger1.setLevel(level)

hdlr1 = logging.FileHandler("./spider1.log")
hdlr1.setLevel(level)
logger1.addHandler(hdlr1)

index = 0


class TtdsBbcSpider(scrapy.Spider):
    name = 'TTDS_BBC'
    allowed_domains = ['bbc.co.uk']
    start_urls = ['https://www.bbc.co.uk/news/coronavirus', 'https://www.bbc.co.uk/news/science-environment-56837908',
                  'https://www.bbc.co.uk/news/england', 'https://www.bbc.co.uk/news/scotland',
                  'https://www.bbc.co.uk/news/northern_ireland', 'https://www.bbc.co.uk/news/wales',
                  'https://www.bbc.co.uk/news/world/africa',
                  'https://www.bbc.co.uk/news/world/asia', 'https://www.bbc.co.uk/news/world/australia',
                  'https://www.bbc.co.uk/news/world/europe', 'https://www.bbc.co.uk/news/world/latin_america',
                  'https://www.bbc.co.uk/news/world/middle_east', 'https://www.bbc.co.uk/news/world/us_and_canada',
                  'https://www.bbc.co.uk/news/technology', 'https://www.bbc.co.uk/news/health',
                  'https://www.bbc.co.uk/news/education', 'https://www.bbc.co.uk/news/entertainment_and_arts']

    def start_requests(self):
        DEFAULT_REQUEST_HEADERS['Accept'] = '*/*'
        DEFAULT_REQUEST_HEADERS['Host'] = 'bbc.co.uk'
        DEFAULT_REQUEST_HEADERS['Referer'] = 'https://bbc.co.uk/'
        for start_url in self.start_urls:
            req = Request(start_url.format(category="news"), callback=self.parse_list, meta={"title": "ContentList"},
                          encoding='utf-8')
            yield req

    # got the page and parse to get list of news
    def parse_list(self, response):
        global index
        if index == 0:
            news_list = response.xpath("//*[@id='lx-stream']/div[1]/ol/li")
        else:
            news_list = response.xpath("//*[@id='lx-stream']/div[2]/ol/li")
        for news in news_list:
            msg = response.meta
            msg['title'] = news.xpath(".//header//h3/a/span/text()").get()
            if news.xpath(".//header//h3/a/@href").get():
                msg['url'] = "https://" + DEFAULT_REQUEST_HEADERS['Host'] + news.xpath(".//header//h3/a/@href").get()
            else:
                continue
            # call parse_content to parse the passage and get content
            logger.info('now in page' + response.request.url + ' and news url is' + msg['url'])
            yield Request(msg["url"], callback=self.parse_content, meta=msg)


    def parse_content(self, response):
        if '/av/' not in response.request.url:
            tag = re.search(r'https://bbc.co.uk/(.*)', response.meta.get("url", ""), re.I).group(1)
            text = response.xpath("//article/div//p//text()").getall()
            content = ''
            # combine sentences
            for i in range(len(text)):
                if i == 0:
                    pass
                else:
                    content += text[i] + ' '
            publish_time = response.xpath("//time/@datetime").get()
            news_item = NewsSpiderItem()
            news_item['headline'] = response.meta.get("title", "")
            news_item['publish_time'] = publish_time
            news_item['content'] = content
            news_item['tag'] = tag
            logger1.info("news_item['title']" + "was submitted")
            yield news_item
        else:
            logger1.info("website {0} is not valid".format(response.meta.get("url", "")))
            pass
