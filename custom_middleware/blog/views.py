from django.shortcuts import render

# Create your views here.

def home(request):
    print('This is Home')
    return render(request, 'blog/home.html')
