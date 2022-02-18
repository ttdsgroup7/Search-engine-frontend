from scrapy import cmdline
import requests
from bs4 import BeautifulSoup
import re

name = 'BBC_news'
cmd1 = 'scrapy crawl {0} -s LOG_FILE=all.log'.format(name)
if __name__ == '__main__':
    cmdline.execute(cmd1.split())
    # url = 'https://www.bbc.co.uk/news/world'
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, 'lxml')
    # for a in soup.find_all('a'):
    #     if(re.match(r'/news/\D+\d+',a['href'])):
    #         print(re.match(r'/news/\D+\d+',a['href']).group())
    # print('*' * 100)
