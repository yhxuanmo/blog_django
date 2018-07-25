from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

from article.models import MyArticle, ReaderComment, ArticleTag
# Create your views here.
def get_article(request):
    """
    返回article页面
    """
    if request.method == 'GET':
        # tag_id = request.GET.get('tag')
        # if tag_id:
        #     return HttpResponseRedirect(reverse('article:get_article_by_tag', args=(tag_id,)))
        return render(request, 'article.html')


def show_all_article(request):
    """
    获取所有文章的接口
    :return: 返回查询结果Json
    """
    if request.method == 'GET':
        articles = MyArticle.objects.all()
        article_list = []
        for article in articles:
            if article.is_show == 1:
                article_info = article.main_to_dict()
                article_list.append(article_info)
        data = {'code':200, 'article_list':article_list}
        return JsonResponse(data=data)


def show_article_by_id(request, id):
    """
    通过文章id获取文章
    :param id: 文章id
    :return: detail页面和文章data
    """
    if request.method == 'GET':
        article_res = MyArticle.objects.filter(id=id).first()
        # data = {'article':article_res.all_to_dict()}
        article_res.count_of_read += 1
        article_res.save()
        data = {'article': article_res}
        return render(request, 'detail.html', data)


def save_user_comment(request, id):
    """
    文章评论
    :param id: 文章id
    :return: Json，包含评论时间
    """
    if request.method == 'POST':
        comment_info = request.POST
        reader_name = comment_info.get('reader_name')
        comment = comment_info.get('comment')
        head_img = comment_info.get('head_img')
        article_id = int(id)
        article = MyArticle.objects.filter(id=article_id).first()
        article.count_of_comment += 1
        reader_comment = ReaderComment.objects.create(reader_name=reader_name,
                                      comment=comment,
                                      head_img=head_img,
                                      article_id_id=article_id)
        article.save()
        data = {'code':200,'comment_time':reader_comment.comment_time}
        return JsonResponse(data)


def show_all_tag(request):
    """
    分类标签请求接口
    :return: json
    """
    if request.method == 'GET':
        tags = ArticleTag.objects.all()
        tag_list = []
        for tag in tags:
            if not tag.is_delete:
                tag_list.append(tag.to_dict())
        data = {'code': 200,'tags': tag_list}
        return JsonResponse(data)


def get_article_by_tag(request, tag_id):
    """
    分类查询文章接口
    :param tag_id: 分类标签id
    :return: json，如果有结果，返回查询结果
    """
    tag_article = MyArticle.objects.filter(tag_id=tag_id)
    if tag_article:
        article_list = []
        for article in tag_article:
            if article.is_show == 1:
                article_info = article.main_to_dict()
                article_list.append(article_info)
        data = {'code': 200, 'article_list': article_list}
    else:
        data= {'code': 0}
    return JsonResponse(data)


