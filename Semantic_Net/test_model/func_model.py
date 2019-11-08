from gensim import models
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

model_path = 'E:/Deeplearning/yipeng_works/deeplearning/synonyms_similarity/synonyms_process/model/wiki_corpus.model'
model = models.Word2Vec.load(model_path)

"""
对于给定的词，找出Top-n最相似的，并且按照相似度排序(Top-n默认100)
return a dictionary: keys-words, value-similarities
"""
def get_most_similar(word, Top_n=100):
    result = model.most_similar(word, topn=Top_n)   # 返回的是一个list-array,
    word_cloud = dict()
    for res in result:
        word_cloud[res[0]] = round(res[1],4)     # res[0]-word, res[1]-similarity
    return word_cloud

"""
计算两个词之间的相似度
return: float
"""
def compus_words_similarity(word1, word2):
    similarity = model.similarity(word1, word2)   #  计算两个词的cosine similarity
    return round(similarity, 4)

"""
计算两个词汇列表的相似度
return: float
"""
def compus_wordlists_similarity(wordlist1, wordlist2):
    similarity_of_lists = model.n_similarity(wordlist1, wordlist2)
    return round(similarity_of_lists, 4)

"""
找出一个单词列表中不同类的词语
return: str
"""

def get_diff_word(wordlist):
    diff = model.doesnt_match(wordlist)
    return diff