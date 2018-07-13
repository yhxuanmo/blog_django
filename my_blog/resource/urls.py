from django.conf.urls import url

from resource import views

urlpatterns=[
    url(r'^$', views.get_resource, name='resource')

]