# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
# from itemadapter import ItemAdapter
# from scrapy import Item


class mysql_pipeline:
    def process_item(self, item, spider):
        self.insert_mysql(item)
        return item

    # connect to the databases
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='35.246.23.112',
                                    port=3306,
                                    user='root',
                                    password='!ttds2021',
                                    db='TTDS_group7',
                                    charset='utf8mb4')
        # self.cursor = self.db.cursor(DictCursor)
        self.cursor = self.conn.cursor()
        self.ori_table = 'BBC_news'

    # Close the databases
    def close_spider(self, spider):
        print("Terminating" + spider.name + "spider...")
        self.cursor.close()
        self.conn.close()
        # self.db_conn.connection_pool.disconnect()

    # Insert the data
    def insert_mysql(self, item):
        sql = '''insert into {0}(Publish_date, Headline, content, Tag)  VALUES ('{1}','{2}','{3}','{4}') '''.format(self.ori_table,
                                                                              item.get(
                                                                                  'publish_time',
                                                                                  ''),
                                                                              pymysql.converters.escape_string(item.get(
                                                                                  'headline',
                                                                                  '')),
                                                                              pymysql.converters.escape_string(
                                                                                  item.get(
                                                                                      'content',
                                                                                      '')),
                                                                              item.get('tag',
                                                                                       ''))
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('successfully writing the data')
        except BaseException as e:
            print(e)
            print("error writing sql:" + sql)