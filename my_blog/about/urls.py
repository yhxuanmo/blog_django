from django.conf.urls import url

from about import views

urlpatterns=[
    url(r'^$', views.get_about, name='about')

]