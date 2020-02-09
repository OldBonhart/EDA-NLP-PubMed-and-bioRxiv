import multiprocessing
import gensim
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import numpy as np
import random
import re

import nltk
from nltk.corpus import stopwords


# Data preparation 

def preprocess_text(text):
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text

def get_sentences(data, site):
    if site == "pubmed":
        text = [i for i in [x[0] for x in data.values()]]
    else:
        text = [i for i in [x[0][0] for x in data.values()]]

    stop_words = stopwords.words('english')
    print("Num articles:", len(text))
    text = "".join(str(text))
    sentences = []
    for sentence in nltk.sent_tokenize(text, "english"): 
        sentence = preprocess_text(sentence).lower()
        clear_text = [word for word in sentence.split() if word not in stop_words]

        clear_text = " ".join(clear_text).strip()
        sentences.append(clear_text.lower().split())

    print("Num senteces:", len(sentences))
    return sentences
    
    
def get_embedds_and_words(model):
    embeddings = []
    words = []

    for word in list(model.wv.vocab):
        embeddings.append(model.wv[word])
        words.append(word)
        
    return embeddings, words
    
    
def get_tsna_2d(embeddings, p=30, n_iter=3500):
    tsne = TSNE(perplexity=p,
                      n_components=2,
                      init='pca', 
                      n_iter=n_iter,
                      random_state=36)
    embeddings_2d = tsne.fit_transform(embeddings)
    return embeddings_2d

def get_tsna_3d(embeddings, p=30, n_iter=3500):
    tsne = TSNE(perplexity=p,
                      n_components=3,
                      init='pca', 
                      n_iter=n_iter,
                      random_state=36)
    embeddings_3d = tsne.fit_transform(embeddings)
    return embeddings_3d
    
    
    
def get_2d_clusters(model,
                    k_words,
                    n_top_words,
                    p=15,
                    n_iter=3200):

    keys = random.choices(list(model.wv.vocab.keys()), k=k_words)

    embedding_clusters = []
    word_clusters = []
    for word in keys:
        embeddings = []
        words = []
        for similar_word, _ in model.most_similar(word, topn=n_top_words):
            words.append(similar_word)
            embeddings.append(model[similar_word])
        embedding_clusters.append(embeddings)
        word_clusters.append(words)

    # Find tsne coordinats for 2 dimensions
    embedding_clusters = np.array(embedding_clusters)
    n, m, k = embedding_clusters.shape
    tsne_model_2d = TSNE(perplexity=p,
                         n_components=2,
                         init='pca',
                         n_iter=n_iter,
                         random_state=36)
    
    embeddings_2d = np.array(tsne_model_2d.fit_transform(embedding_clusters.reshape(n * m, k))).reshape(n, m, 2)

    return keys, embeddings_2d, word_clusters