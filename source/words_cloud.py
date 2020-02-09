from PIL import Image
import numpy as np
import copy
import matplotlib.pyplot as plt


from wordcloud import WordCloud, STOPWORDS
from collections import Counter
from nltk.corpus import stopwords
import nltk


def makeWordCloud(numWords, data, img_name, mask=None, color=None):
    topic_words = [ z.lower() for y in
                        [ x[0] for x in data.values()]
                        for z in y]
    word_count_dict = dict(Counter(topic_words))
    popular_words = sorted(word_count_dict, key = word_count_dict.get, reverse = True)
    popular_words_nonstop = [w for w in popular_words if w not in stopwords.words("english")]
    
    word_string=str(popular_words_nonstop)
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='black',
                          max_words=numWords,
                          width=1600, height=1080,
                          mask=mask,
                          contour_width=3, 
                          contour_color=color,
                         ).generate(word_string)

    wordcloud.to_file(f"{img_name}.png")

    return wordcloud