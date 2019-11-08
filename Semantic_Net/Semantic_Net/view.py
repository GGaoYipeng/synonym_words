"""
simple: 数据和视图混合
"""
# from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse("Hello world ! ")

"""
use Templates: MVC架构-数据视图分离
"""
from django.shortcuts import render, render_to_response
from test_model.func_model import *
from django.http.response import HttpResponse

def main(request):
    context = dict()
    context['hello'] = 'Welcome to 语义计算-同义词近义词!'
    return render(request, 'homepage.html', context)

def similarwords(request):
    if request.method == 'POST':
        search_word1 = request.POST.get("word1")
        search_word2 = request.POST.get("word2")
        context = dict()    # render 使用一个字典context作为参数
        # context['hello'] = 'Hello World!'   # data
        # context 字典中元素的键值 "hello" 对应了模板中的变量 "{{ hello }}"
        context['similarity_words'] = compus_words_similarity(search_word1, search_word2)
        return render(request, 'similarwords.html', context)
    else:
        return render_to_response('similarwords.html')

def similarlists(request):
    if request.method == 'POST':
        search_list1 = request.POST.get("list1").split(' ')
        search_list2 = request.POST.get("list2").split(' ')
        context = dict()  # render 使用一个字典context作为参数
        context['similarity_lists'] = compus_wordlists_similarity(search_list1, search_list2)
        return render(request, 'similarlists.html', context)
    else:
        return render_to_response('similarlists.html')

def differentword(request):
    if request.method == 'POST':
        search_list = request.POST.get("list").split(' ')
        context = dict()  # render 使用一个字典context作为参数
        context['differet_word'] = get_diff_word(search_list)
        return render(request, 'differentword.html', context)
    else:
        return render_to_response('differentword.html')

def sysnonymwords(request):
    if request.method == 'POST':
        search_word = request.POST.get("word")
        context = dict()  # render 使用一个字典context作为参数
        context['synonyms_lists'] = get_most_similar(search_word)
        return render(request, 'synonymwords.html', context)
    else:
        return render_to_response('synonymwords.html')