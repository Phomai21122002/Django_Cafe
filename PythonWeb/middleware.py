from django.conf import settings
from django.shortcuts import redirect

def LoginRequiredMiddleware(get_response):

    def __init__(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
        
    #     # if ('admin/' not in request.path) and (request.session.get('id') != None) :
    #     #     print(request.session.get('id'))
    #     #     del request.session['id']
    #     response = self.get_response(request)
    #     return response
    
    def middleware(request):
        if ('admin/' in request.build_absolute_uri()) and (request.session.get('id') == None):
            return redirect('Home:Login')
        if 'Referer' in request.headers:
            pass
        else:
            if not ('admin/' in request.path) and request.session.get('id') != None:
                del request.session['id']
        response = get_response(request)
        return response
    return middleware
