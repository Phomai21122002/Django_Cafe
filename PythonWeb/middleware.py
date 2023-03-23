from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, required):
        response = self.get_response(required)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = view_func.__name__
        print(view_name)
        pass
        
            

