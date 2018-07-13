from django.conf.urls import url

from article import views

urlpatterns=[
    url(r'^$', views.get_article, name='article')

]