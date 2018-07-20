from django.conf.urls import url

from article import views

urlpatterns=[
    url(r'^$', views.get_article, name='article'),
    url(r'^all/', views.show_all_article),
    url(r'detail/(?P<id>[0-9]+)/$', views.show_article_by_id),
    url(r'detail/(?P<id>[0-9]+)/comment/$', views.save_user_comment),

]