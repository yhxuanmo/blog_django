from django.conf.urls import url
from my_background import views

urlpatterns = [
    url(r'^/$',views.get_background),
    url(r'^/page/main/',views.get_bg_main),
]