# Write your code here
from sklearn.feature_extraction.text import TfidfVectorizer
from lxml import etree
import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re
import numpy as np

root = etree.parse("news.xml").getroot()
nd = dict()
lemmatize = WordNetLemmatizer().lemmatize
not_cool = stopwords.words("English") + list(string.punctuation)

news_tokens = []
for news in root[0]:
    tokens = sorted(nltk.word_tokenize(news[1].text.lower()), reverse=True)
    tokens = [lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in not_cool]
    tokens = [word for word in tokens if nltk.pos_tag([word])[0][1] == "NN"]
    news_tokens += [" ".join(tokens)]

vectorizer = TfidfVectorizer(input='content', use_idf=True, lowercase=True, analyzer='word', ngram_range=(1, 1), stop_words=None)
model = vectorizer.fit_transform(news_tokens).toarray()
feature_names = vectorizer.get_feature_names()

for i in range(len(root[0])):
    sorted_indices = np.argsort(model[i,:])
    top_dict = {feature_names[j]: model[i, j] for j in sorted_indices[-10:]}
    top_dict = sorted(top_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    top_five = " ".join(x[0] for x in top_dict[:5])
    head = root[0][i][0].text
    print(head + ":", top_five, sep="\n", end='\n\n')
