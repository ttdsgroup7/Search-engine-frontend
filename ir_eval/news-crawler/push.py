import json
import os

import pymysql


def connectMysql():
    connMysql = pymysql.connect(
        host='34.89.114.242',
        port=3306,
        user='root',
        password='!ttds2021',
        db='TTDS_group7',
        charset='utf8mb4'
    )
    return connMysql


def execute(sentence, commitlist):
    conn = connectMysql()
    cursor = conn.cursor()
    cursor.executemany(sentence, commitlist)
    conn.commit()
    conn.close()


theme = {
    'Business': 'business',
    'Health': 'health',
    'Well': 'health',
    'Technology': 'tech',
    'Climate': 'climate',
    'Briefing': 'entertainment',
    'Entertainment': 'entertainment',
    'Science': 'science',
    'Politics': 'politics',
    'Education': 'education',
    'Sports': "world",
    'Arts': 'world'
}
# { "title": "Will the Excelsior Pass, New York\u2019s Vaccine Passport, Catch On? - The New York Times",
# "published_date": "2021-06-01T07:00:10.000Z", "section": "New York", "content": "On the Upper East Side in
# Manhattan" "link": "https://www.nytimes.com/2021/06/01/nyregion/excelsior-pass-vaccine.html",
# "image": "https://static01.nyt.com/images/2021/05/27/nyregion/00nyvirus-excelsior/00nyvirus-excelsior-articleLarge}
if __name__ == '__main__':
    base = './dataset/nytimes/'
    year = os.listdir(base)
    handle = []
    for i in year:
        cur = base + i + '/'
        month = os.listdir(cur)
        for j in month:
            day_ = cur + j + '/'
            day = os.listdir(day_)
            for k in day:
                target = day_ + k + '/articles'
                f = open(target, 'r')
                handle.extend(json.load(f)['articles'])
                f.close()

    sentence = 'insert IGNORE into news(Publish_date,head_line,content,image,theme,url) values ((%s),(%s),(%s),' \
               '(%s),(%s),(%s)) '
    commitlist = []
    last_date = '2022-02-01 12:00:00'
    for i in handle:
        # j: (title,published_date,section,content,link,image)
        # tb:(date,title,content,country,image,theme,url)
        tmp_theme = 'world'
        tmp_date = last_date
        if i['section'] in theme:
            tmp_theme = theme[i['section']]
        if i['published_date'] is not None:
            tmp_date = i['published_date'].replace('T', ' ')[:-5]
        commitlist.append((tmp_date, i['title'], i['content'], i['image'], tmp_theme, i['link']))

    if len(commitlist) > 10000:
        i = 0
        while i<len(commitlist):
            part = commitlist[i:i + 10000]
            execute(sentence,part)
            i+=10000
            print("query {} finished".format(i))
    else:
        execute(sentence,commitlist)
    print('finished')

