import json

from nltk.corpus import reuters
import nltk
from collections import defaultdict
import string
# get reuter corpus and categories
# nltk.download('reuters')
# nltk.download('punkt')

category = reuters.categories()
# retrieve all categories
corpus = reuters.sents(categories=category)

# frequency of single word
term_count = defaultdict(int)
# frequency of Bi-words
bigram_count = defaultdict(int)
# traverse by doc
for doc in corpus:
    doc = [i.lower() for i in doc]
    # last char is dot, can be ignored
    for i in range(0, len(doc) - 1):
        term = doc[i]
        bigram = doc[i:i + 2]
        if term not in string.punctuation:
            term_count[term] += 1
        bigram = ' '.join(bigram)
        bigram_count[bigram] += 1

with open('oxford.txt','r',encoding='utf-8') as f:
    txt = f.readlines()
for j in txt:
    st = j.strip().lower().split(" ")
    for i in range(len(st)-1):
        term = st[i]
        bigram = st[i:i + 2]
        if term not in string.punctuation:
            term_count[term] += 1
        bigram = ' '.join(bigram)
        bigram_count[bigram] += 1
    term = st[len(st)-1]
    if term not in string.punctuation:
        term_count[term] += 1



tc = json.dumps(term_count)
bc = json.dumps(bigram_count)

with open('term_count.json','w',encoding='utf-8') as f:
    f.write(tc)
with open('bigram_count.json','w',encoding='utf-8') as f:
    f.write(bc)
