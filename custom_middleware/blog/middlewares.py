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


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    # if the 'process_view' returns an 'HttpResponse'
    # then the 'View' will not be called
    # if the 'process_view' returns 'None'
    # then the 'View' will be called
    def process_view(request, *args, **kwargs):
        print('This is the Process View - before View')
        # return HttpResponse('This is before view')
        return None


class MyProcessExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    # goes to work when an exception is encountered in 'View'
    def process_exception(self, request, exception):
        print('Exception Occured')
        message = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(message)


class MyProcessTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    # changes the 'context' value in 'View'
    def process_template_response(self, request, response):
        print('Process Template Response from Middleware')
        response.context_data['course'] = 'python'
        return response
