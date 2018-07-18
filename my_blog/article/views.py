from django.http import JsonResponse
from django.shortcuts import render

from article.models import MyArticle
# Create your views here.
def get_article(request):
    if request.method == 'GET':
        return render(request, 'article.html')


def show_all_article(request):
    if request.method == 'GET':
        articles = MyArticle.objects.all()
        article_list = []
        for article in articles:
            article_info = article.main_to_dict()
            article_list.append(article_info)
        data = {'code':200, 'article_list':article_list}
        return JsonResponse(data=data)





def show_article_by_id(request, id):
    if request.method == 'GET':
        article_res = MyArticle.objects.filter(id=id).first()
        # data = {'article':article_res.all_to_dict()}
        data = {'article': article_res}


        return render(request, 'detail.html', data)


