from django.shortcuts import render

# Create your views here.


def get_timeline(request):
    if request.method == 'GET':
        return render(request, 'timeline.html')