# Write your code here
from lxml import etree
import nltk
from collections import Counter

root = etree.parse("news.xml").getroot()
nd = dict()

for news in root[0]:
    head = news[0].text
    tokens = nltk.word_tokenize(news[1].text.lower())
    cd = sorted(Counter(tokens).items(), reverse=True, key=lambda x: (x[1], x[0]))
    top_five = " ".join([x[0] for x in cd[:5]])
    print(head + ":", top_five, sep="\n", end='\n\n')

