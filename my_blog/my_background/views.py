from django.shortcuts import render

# Create your views here.
def get_background(request):
    if request.method == 'GET':
        return render(request, 'bg/index.html')

def get_bg_main(request):
    if request.method == 'GET':
        return render(request, 'bg/page/main.html')

def get_bg_newslist(request):
    if request.method == 'GET':
        return render(request, 'bg/page/news/newsList.html')

def bg_news_add(request):
    if request.method == 'GET':
        return render(request, 'bg/page/news/newsAdd.html')


def get_bg_linkslist(request):
    if request.method == 'GET':
        return render(request, 'bg/page/links/linksList.html')


def bg_links_add(request):
    if request.method == 'GET':
        return render(request, 'bg/page/links/linksAdd.html')


def get_bg_404(request):
    if request.method == 'GET':
        return render(request, 'bg/page/404.html')

def get_bg_system_parameter(request):
    if request.method == 'GET':
        return render(request, 'bg/page/systemParameter/systemParameter.html')

def get_user_info(request):
    if request.method == 'GET':
        return render(request, 'bg/page/user/userInfo.html')

def user_change_passwd(request):
    if request.method == 'GET':
        return render(request, 'bg/page/user/changePwd.html')


def get_all_user(request):
    if request.method == 'GET':
        return render(request, 'bg/page/user/allUsers.html')

def add_user(request):
    if request.method == 'GET':
        return render(request, 'bg/page/user/addUser.html')

def get_message(request):
    if request.method == 'GET':
        return render(request, 'bg/page/message/message.html')

def message_reply(request):
    if request.method == 'GET':
        return render(request, 'bg/page/message/messageReply.html')

def get_images(request):
    if request.method == 'GET':
        return render(request,'bg/page/img/images.html' )
