from django.http import HttpResponse


class SevoMaintainanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before view
        print("SMM", request.user)
        print("SMM", request.path)
        
        if not "admin" in request.path and not request.user.is_superuser:
            return HttpResponse("SEVO MAINTAINANCE")

        #return HttpResponse("SEVO MAINTAINANCE")
        response = self.get_response(request)
        # after view

        return response