from django.shortcuts import render

# Create your views here.
def get_home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
