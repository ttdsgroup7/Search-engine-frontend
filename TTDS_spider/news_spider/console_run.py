from scrapy import cmdline

name = 'TTDS_BBC'
cmd1 = 'scrapy crawl {0}'.format(name)
if __name__ == '__main__':
    cmdline.execute(cmd1.split())