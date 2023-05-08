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
    
    def middleware(request):        # print(request.session.get('id'))
        if ('admin/' in request.build_absolute_uri()) and (request.session.get('id') == None):
            return redirect('Home:Login')
        
        if ('staff/' in request.build_absolute_uri()) and (request.session.get('id') == None):
            return redirect('Home:Login')
        # print(request.headers)
        if 'Referer' in request.headers:
            pass
        else:
            # print('khong')
            if not ('admin/' and 'staff/' in request.path) and request.session.get('id') != None:
                del request.session['id']
                return redirect('Home:Login')
        response = get_response(request)
        return response
    return middleware
