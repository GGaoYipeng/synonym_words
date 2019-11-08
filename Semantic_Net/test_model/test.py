import logging
from gensim import models
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

'''
获取一个圆形的mask
'''
def get_mask():
    x, y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    return mask

'''
绘制词云
'''
# logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
# /home/yipeng/works/deeplearning/synonyms_similarity/data/word2vec/news_12g_baidubaike_20g_novel_90g_embedding_64.model
# E:/Deeplearning/yipeng_works/deeplearning/synonyms_similarity/word2vec_model/model/wiki_corpus.model
model_path = './model/wiki_corpus_500vec.model'
print('model path: ', model_path)
model = models.Word2Vec.load(model_path)
# 输入一个词找出相似的前100个词
one_corpus = ["人工智能"]
result = model.most_similar(one_corpus[0], topn=100)
# 将返回的结果转换为字典,便于绘制词云
word_cloud = dict()
print("---------计算一个词的最近似词，TOP100---------")
for sim in result:
    print(sim[0], ":", sim[1])
    word_cloud[sim[0]] = sim[1]
# 绘制词云
font = 'E:/Deeplearning/yipeng_works/python/dd/dd/msyh.ttf'
wc = WordCloud(background_color="white", mask=get_mask(), font_path=font)
wc.generate_from_frequencies(word_cloud)
# 隐藏x轴和y轴
plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()
wc.to_file('similar_words.png')

# #输入两个词计算相似度
two_corpus = ["数学", "微积分"]
res = model.similarity(two_corpus[0], two_corpus[1])
print("---------计算两个词之间的余弦相似度---------")
print(two_corpus)
print("similarity of two words:%.4f" % res)

# 获得一个词的词向量
test_words1 = ['人工智能', '计算机', '自然语言']
test_words2 = ['编程', '神经网络', '计算能力']
print("---------获取单个词的词向量---------")
print("test_words: ", test_words1[0])
print("词向量：", model[test_words1[0]])

# 两个集合之间的余弦相似度
similarity_of_lists = model.n_similarity(test_words1, test_words2)
print("---------计算两个集合之间的余弦相似度---------")
print("list 1: ", test_words1)
print("list 2: ", test_words2)
print("similarity of two lists: %.4f" % similarity_of_lists)

# 选出集合中不同类的词语
print("---------选出集合中不同类的词语---------")
test_words3 = ['足球', '篮球', '乒乓球', '鲜花']
print("list: ", test_words3)
diff = model.doesnt_match(test_words3)
print("different object: ", diff)

# 两个集合做差

list1 = ['女人', '国王']
list2 = ['男人']
print("---------两个集合做差---------")
tmp = model.most_similar(positive=list1, negative=list2, topn=2)
print(tmp)

# # 输入三个词类比
# three_corpus = ["北京", "上海", "广州"]
# res = model.most_similar([three_corpus[0], three_corpus[1], three_corpus[2]], topn=100)
# # 将返回的结果转换为字典,便于绘制词云
# word_cloud = dict()
# for sim in res:
#     # print(sim[0],":",sim[1])
#     word_cloud[sim[0]] = sim[1]
# # 绘制词云

# Process finished with exit code 139 (interrupted by signal 11: SIGSEGV) 报错：执行无效的内存引用
# MemoryError 怎么解决？

