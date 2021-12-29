import json
import pymysql
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
from collections import defaultdict

# download data once
# nltk.download('stopwords')

# pre process, will return a list of inverted list, format like {"example":{1:{4,2,7},2:{1,4,6}},...}
def preprocess(text):
    inverted = defaultdict(lambda: defaultdict(list))
    # record headline length, increase its weight in tfidf
    headlen = {}
    for i in text:
        id = i[2]
        head = re.findall(r'[0-9a-zA-Z]+', i[0].lower())
        content = re.findall(r'[0-9a-zA-Z]+', i[1].lower())
        head = [ps.stem(j) for j in head if j not in sw]
        content = [ps.stem(j) for j in content if j not in sw]
        hl = len(head)
        doc = head + content
        for index, term in enumerate(doc):
            inverted[term][id].append(index)
        headlen[id] = hl

    toinsert = [(i,json.dumps(j)) for i,j in inverted.items()]
    sentence = 'insert into inverted(term,list) values(%s,%s)'
    cursor.execute('truncate inverted')
    cursor.executemany(sentence, toinsert)
    cursor.execute('truncate headlen')
    sentence = 'insert into headlen(id,len) values(%s,%s)'
    cursor.executemany(sentence,tuple(headlen.items()))
    print()


if __name__ == '__main__':
    # use set to speed up, O(1)
    sw = set(stopwords.words('english'))
    ps = PorterStemmer()
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
    sentence = 'select headline,content,id from test'
    # this can only get count
    cursor.execute(sentence)
    # get nested tuple of results
    # t[0] the first res
    text = cursor.fetchall()
    preprocess(text)
    conn.commit()
    conn.close()