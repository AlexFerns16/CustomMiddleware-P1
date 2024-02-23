from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print('This is a Home View')
    return render(request, 'blog/home.html')

def exception(request):
    print('This is an Exception View')
    a = 10/0
    return HttpResponse('This is an Exception Page')

def userinfo(request):
    print('This is a User Info View')
    context = {
        'course':'django'
    }
    return TemplateResponse(request, 'blog/userinfo.html', context)
