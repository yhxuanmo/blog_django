from django.shortcuts import render

# Create your views here.


def get_resource(request):
    if request.method == 'GET':
        return render(request, 'resource.html')