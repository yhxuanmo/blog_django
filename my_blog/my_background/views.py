from django.shortcuts import render

# Create your views here.
def get_background(request):
    if request.method == 'GET':
        return render(request, 'bg/index.html')

def get_bg_main(request):
    if request.method == 'GET':
        return render(request, 'bg/page/main.html')