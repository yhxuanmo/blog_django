from django.conf.urls import url

from timeline import views

urlpatterns=[
    url(r'^$', views.get_timeline, name='timeline')

]