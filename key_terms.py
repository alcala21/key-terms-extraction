# Write your code here
from lxml import etree
import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re

root = etree.parse("news.xml").getroot()
nd = dict()
lemmatize = WordNetLemmatizer().lemmatize
not_cool = stopwords.words("English") + list(string.punctuation)

for news in root[0]:
    head = news[0].text
    tokens = sorted(nltk.word_tokenize(news[1].text.lower()), reverse=True)
    tokens = [lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in not_cool]
    cd = Counter(tokens).most_common(5)
    top_five = " ".join(x[0] for x in cd)
    print(head + ":", top_five, sep="\n", end='\n\n')
