import json
import sys

import geograpy
import pymysql
from tenacity import retry, stop_after_attempt

# covert nation name to needed name
convert_dict = {
    "People's Republic of China": 'China',
    'The Gambia': 'Gambia',
    'Guinea-Bissau': 'Guinea Bissau',
    'North Macedonia': 'Macedonia',
    'Serbia': 'Republic of Serbia',
    'Eswatini': 'Swaziland',
    'Tanzania': 'United Republic of Tanzania'
}


class Nation():
    text = ''
    res = []
    id = []
    cur =0

    def __init__(self,cur):
        self.cur = cur

    def connectMysql(self):
        connMysql = pymysql.connect(
            host='34.89.114.242',
            port=3306,
            user='root',
            password='!ttds2021',
            db='TTDS_group7',
            charset='utf8mb4'
        )
        return connMysql

    @retry(stop=stop_after_attempt(5))
    def execute(self, sentence, commitlist):
        conn = self.connectMysql()
        cursor = conn.cursor()
        cursor.executemany(sentence, commitlist)
        conn.commit()
        conn.close()

    def executeall(self):
        # print("abstract: ", res[0])
        # print("id: ",id[curindex])
        sentence = 'update news set country=(%s) where id = (%s)'
        commitlist = []
        for index in range(len(self.res)):
            commitlist.append((self.res[index], self.id[index]))

        if len(commitlist) > 10000:
            i = 0
            while i < len(commitlist):
                part = commitlist[i:i + 10000]
                self.execute(sentence, part)
                i += 10000
                print("query {} finished".format(i))
        else:
            self.execute(sentence, commitlist)

    def get_data(self):
        conn = self.connectMysql()
        cursor = conn.cursor()
        sentence = 'select id,content from news where country is null and id>%s limit 30'
        cursor.execute(sentence,self.cur)
        self.text = dict(cursor.fetchall())
        self.id = list(self.text.keys())
        conn.close()
        return self.id

    def get_name(self):
        alldata = self.text.values()
        for i in alldata:
            nation = geograpy.get_geoPlace_context(text=i).countries
            if not nation:
                self.res.append('None')
            else:
                if nation[0] in convert_dict:
                    nation[0] = convert_dict[nation[0]]
                self.res.append(nation[0])

    def save(self, name, data):
        f = open(name, 'w')
        json.dump(data, f)
        f.close()

    def clear(self):
        self.id = []
        self.res = []
        self.text = dict()

    def readfromfile(self, name):
        with open(name, 'r') as f:
            self.text = json.load(f)
            self.id = list(self.text.keys())
            self.res = list(self.text.values())
            for i in range(len(self.res)):
                if self.res[i] in convert_dict:
                    self.res[i] = convert_dict[self.res[i]]
            self.executeall()

cur = 0
if len(sys.argv)>1:
    cur = sys.argv[1]
a = Nation(cur)
# a.readfromfile('nation.json')
start = 0
while a.get_data():
    a.get_name()
    # a.save(str(start) + 'backup_nation.json', dict(zip(a.id, a.res)))
    a.executeall()
    a.clear()
    start += 1
    print("part {} finished".format(start))
