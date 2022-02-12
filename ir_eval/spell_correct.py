from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

a =["""Yesterday I went fishing. I don't fish that often, 
so I didn't catch any fish. I was told I'd enjoy myself, 
but it didn't really seem that fun but it."""]

# use this to add one-character word
# vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")

# split sentence by punctuation and ignore single char
b = CountVectorizer(ngram_range=(2,2))
c=b.fit_transform(a)
# print(c)

res = pd.DataFrame(c.toarray(),columns=b.get_feature_names_out())
print(res['but it'])