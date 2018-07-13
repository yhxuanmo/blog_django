from django.shortcuts import render

# Create your views here.
def get_article(request):
    if request.method == 'GET':
        return render(request, 'article.html')