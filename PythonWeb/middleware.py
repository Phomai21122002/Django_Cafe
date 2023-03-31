from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if ('admin/' in request.path) and (request.session.get('id') == None) :
            return redirect('Home:Login')
        if ('admin/' not in request.path) and (request.session.get('id') != None) :
            del request.session['id']
        response = self.get_response(request)
        return response
    
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print(f'view admin: {view_func.__name__}')
    #     if (view_func.__name__ == 'index') {
            
    #     }
    #     pass