from django.conf.urls import url
from my_background import views

urlpatterns = [
    url(r'^/$',views.get_background, name='background'),
    url(r'^/page/main/',views.get_bg_main),
    url(r'^/page/news/newsList/',views.get_bg_newslist),
    url(r'^/page/news/newsAdd/',views.bg_news_add),

    url(r'^/page/links/linksList/',views.get_bg_linkslist),
    url(r'^/page/links/linksAdd/',views.bg_links_add),

    url(r'^/page/404/',views.get_bg_404),
    url(r'^/page/systemParameter/systemParameter/',views.get_bg_system_parameter),

    url(r"/page/user/userInfo/",views.get_user_info),
    url(r"/page/user/changePwd/",views.user_change_passwd),
    url(r"/page/user/allUsers/",views.get_all_user),
    url(r"/page/user/addUser/",views.add_user),


    url(r"/page/message/",views.get_message),
    url(r"/page/messageReply/",views.message_reply),

    url(r"/page/images/",views.get_images),


]