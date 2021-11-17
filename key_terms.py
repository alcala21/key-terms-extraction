# Write your code here
from lxml import etree
import nltk
from collections import Counter

root = etree.parse("news.xml").getroot()
nd = dict()

for news in root[0]:
    head = news[0].text
    tokens = sorted(nltk.word_tokenize(news[1].text.lower()), reverse=True)
    cd = Counter(tokens).most_common(5)
    top_five = " ".join(x[0] for x in cd)
    print(head + ":", top_five, sep="\n", end='\n\n')
