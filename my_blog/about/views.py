from django.shortcuts import render

# Create your views here.


def get_about(request):
    if request.method == 'GET':
        return render(request, 'about.html')
