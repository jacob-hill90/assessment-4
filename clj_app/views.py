from django.shortcuts import render

def index(request):
    response = render(request, 'clj_app/index.html')
    return response