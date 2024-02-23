from django.shortcuts import HttpResponse

# Create your middlewares here.


def simple_middleware(get_response):
    print("One Time Initialization Function SimpleMiddleware")
    
    def middleware(request):
        print('This is before View Function SimpleMiddleware')
        response = get_response(request)
        print('This is after View Function SimpleMiddleware')
        return response
    return middleware


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization Class SimpleMiddleware")
    
    def __call__(self, request):
        print('This is before View Class SimpleMiddleware')
        response = self.get_response(request)
        print('This is after View Class SimpleMiddleware')
        return response


class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization Class FirstMiddleware")
    
    def __call__(self, request):
        print('This is before View Class FirstMiddleware')
        response = self.get_response(request)
        print('This is after View Class FirstMiddleware')
        return response

    
class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization Class SecondMiddleware")
    
    def __call__(self, request):
        print('This is before View Class SecondMiddleware')
        response = HttpResponse('<h1>Stopped by SecondMiddleware</h1>')
        print('This is after View Class SecondMiddleware')
        return response


class ThirdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization Class ThirdMiddleware")
    
    def __call__(self, request):
        print('This is before View Class ThirdMiddleware')
        response = self.get_response(request)
        print('This is after View Class ThirdMiddleware')
        return response
