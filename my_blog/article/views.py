from django.http import JsonResponse
from django.shortcuts import render

from article.models import MyArticle, ReaderComment
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


def save_user_comment(request, id):
    if request.method == 'POST':
        comment_info = request.POST
        reader_name = comment_info.get('reader_name')
        comment = comment_info.get('comment')
        head_img = comment_info.get('head_img')
        article_id = int(id)
        reader_commment=ReaderComment.objects.create(reader_name=reader_name,
                                      comment=comment,
                                      head_img=head_img,
                                      article_id_id=article_id)
        data = {'code':200,'comment_time':reader_commment.comment_time}
        return JsonResponse(data)
