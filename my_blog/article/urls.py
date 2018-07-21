from django.conf.urls import url

from article import views

urlpatterns=[
    url(r'^$', views.get_article, name='article'),
    url(r'^all/', views.show_all_article),
    url(r'detail/(?P<id>[0-9]+)/$', views.show_article_by_id),
    url(r'detail/(?P<id>[0-9]+)/comment/$', views.save_user_comment),
    url(r'tags/$', views.show_all_tag),
    url(r'tag/(?P<tag_id>[0-9]+)/', views.get_article_by_tag, name='get_article_by_tag'),


]