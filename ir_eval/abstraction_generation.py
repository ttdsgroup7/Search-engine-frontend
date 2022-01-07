import pymysql
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
from transformers import BartForConditionalGeneration, BartTokenizer
from time import time
from collections import defaultdict
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


class Abstraction_Generation():
    src_text = defaultdict(list)
    device = 'cpu'
    res = []
    part = 0
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    def set_text(self, text):
        cnt = 0
        s = list(text)
        for i in s:
            if cnt<100:
                cnt+=1
            else:
                self.part += 1
                cnt = 1
            self.src_text[self.part].append(i.replace('@', ''))




    # device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # xsum used to generate one sentence, ideal for title prediction
    def Pegasus(self):
        model_name = 'google/pegasus-xsum'  # 'google/pegasus-large'
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(self.device)
        batch = tokenizer(self.src_text, truncation=True, padding='longest', return_tensors="pt").to(self.device)
        # model.generate(batch['input_ids'],max_length=...,min_length=...)
        # length is sum of token, not words
        translated = model.generate(**batch, min_length=30, max_length=100)
        return tokenizer.batch_decode(translated, skip_special_tokens=True)

    # generate several sentences, ideal for abstraction

    # BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text.
    # generate for 380 files fail, load 200 at a time
    def Bart(self):
        # facebook/bart-base 2.1GB
        # distilbart-xsum-12-1 400MB
        # https://huggingface.co/sshleifer/distilbart-cnn-12-6 speed
        model_name = "./distilbart-xsum-12-1"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        # forced_bos_token_id =0 disable support for multilingual models
        model = BartForConditionalGeneration.from_pretrained(model_name, forced_bos_token_id=0).to(self.device)
        for i in range(self.part+1):
            print("part {} start".format(i))
            batch = tokenizer(self.src_text[i], truncation=True, padding='longest', return_tensors='pt').to(self.device)
            translated = model.generate(batch['input_ids'], min_length=50, max_length=100)
            # same effect
            # print([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in translated])
            self.res.extend(tokenizer.batch_decode(translated, skip_special_tokens=True, clean_up_tokenization_spaces=False))
        return self.res

    def fill_mask(self):
        model = BartForConditionalGeneration.from_pretrained("facebook/bart-large", forced_bos_token_id=0)
        tok = BartTokenizer.from_pretrained("facebook/bart-large")
        example_english_phrase = "My friends are <mask> but they eat too many carbs."
        batch = tok(example_english_phrase, return_tensors='pt')['input_ids']
        logits = model(batch).logits
        # find index
        mask = (batch[0] == tok.mask_token_id).nonzero().item()
        probs = logits[0, mask].softmax(dim=0)
        values, predictions = probs.topk(5)
        print(tok.decode(predictions).split())
        # batch = tok(example_english_phrase, return_tensors='pt')
        # generated_ids = model.generate(batch['input_ids'])
        # return tok.batch_decode(generated_ids, skip_special_tokens=True)


if __name__ == '__main__':
    conn =connectMysql()
    cursor = conn.cursor()
    sentence = 'select docid,content from to_push'
    cursor.execute(sentence)
    text = cursor.fetchall()
    conn.close()

    text = dict(text)
    test = Abstraction_Generation()
    test.set_text(text.values())
    res = test.Bart()

    id = list(text.keys())
    sentence = 'update to_push set abstract=(%s) where docid = (%s)'
    commitlist = []
    for index in range(len(text)):
        commitlist.append((res[index],id[index]))

    conn = connectMysql()
    cursor = conn.cursor()
    cursor.executemany(sentence,commitlist)
    conn.commit()
    conn.close()

    # for i in text.keys():
    #     text[i] =
    # print(test.Pegasus())
    # print(test.fill_mask())
    # conn.commit()
    # conn.close()

    # from transformers import pipeline
    # print(time())
    # summarizer = pipeline('summarization')
    # print(summarizer(t,min_length=30,max_length=100))
    # print(time())
