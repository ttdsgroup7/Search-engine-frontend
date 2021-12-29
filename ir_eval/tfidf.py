import json
import pymysql
import math
from collections import defaultdict


def calc_tfidf():
    for i, j in text.items():
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


if __name__ == '__main__':
    conn = pymysql.connect(
        host='35.246.23.112',
        port=3306,
        user='root',
        password='!ttds2021',
        db='TTDS_group7',
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    # column name: publish date; headline; content; tag(uri); id
    sentence = 'select * from inverted'
    # this can only get count
    cursor.execute(sentence)
    # get nested tuple of results
    # t[0] the first res
    text = cursor.fetchall()
    sentence = 'select * from headlen'
    # total doc number
    length = cursor.execute(sentence)
    head = cursor.fetchall()

    # get dict of head length
    head = dict(head)
    text = dict(text)
    for i in text:
        text[i] = json.loads(text[i])

    # store tfidf value
    res = defaultdict(lambda: defaultdict(int))
    calc_tfidf()

    # write into database
    # for i, j in res.items():
    #



    conn.commit()
    conn.close()
