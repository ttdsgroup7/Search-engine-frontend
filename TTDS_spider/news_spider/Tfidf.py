import pymysql
import redis
import math
import re
from collections import defaultdict

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk

class Tfidf :

    # connect msyql
    def connectMysql(self):
        connMysql = pymysql.connect(
            host='35.246.23.112',
            port=3306,
            user='root',
            password='!ttds2021',
            db='TTDS_group7',
            charset='utf8mb4'
        )
        return connMysql

    # connect redis
    def connectRedis(self):
        connRedis = redis.Redis(
            host='18.134.241.115',
            port=6379,
            password='!ttds2021')
        return connRedis

    def inverted(self):
        sw = set(stopwords.words('english'))
        ps = PorterStemmer()

        # obtain data from mysql
        cursor = self.connectMysql().cursor()
        sentence = 'select head_line,content,docid from BBC_news'
        cursor.execute(sentence)
        text = cursor.fetchall()
        cursor.close()

        # record headline length, increase its weight in tfidf
        inverted = defaultdict(lambda: defaultdict(list))
        headlen = {}
        for i in text:
            id = i[2]
            head = re.findall(r'[a-zA-Z]+', i[0].lower())
            content = re.findall(r'[a-zA-Z]+', i[1].lower())
            head = [ps.stem(j) for j in head if j not in sw]
            content = [ps.stem(j) for j in content if j not in sw]
            hl = len(head)
            doc = head + content
            for index, term in enumerate(doc):
                inverted[term][id].append(index)
            headlen[id] = hl

        return inverted, headlen

    def calc_tfidf(self, inverted, head):
        length = len(head)
        res = defaultdict(lambda: defaultdict(int))

        for i, j in inverted.items():
            df = len(j)
            for k, v in j.items():
                tf = 0
                for index in v:
                    # increase the weight of the headline
                    if index < head[k]:
                        tf += 5
                    else:
                        tf += 1
                val = (1 + math.log(tf, 10)) * math.log(length / df, 10)
                res[i][k] += val
        return res

    def updateTFIDF(self):
        inverted, headlen = self.inverted()
        res = self.calc_tfidf(inverted, headlen)

        connredis = self.connectRedis()

        with connredis.pipeline(transaction=False) as ctx:
            for word, docs in res.items():
                for docid, pos in docs.items():
                    ctx.hset(word, docid, pos)
            ctx.execute()
        connredis.close()

    def writeStopWordToRedis(self):
        connredis = self.connectRedis()
        sw = set(stopwords.words('english'))
        with connredis.pipeline(transaction=False) as ctx:
            for word in sw:
                ctx.rpush("STOPWRODS", word)
            ctx.execute()
        connredis.close()


if __name__ == '__main__':
    nltk.download('stopwords')
    tfidf = Tfidf()
    # tfidf.writeStopWordToRedis()
    tfidf.updateTFIDF()