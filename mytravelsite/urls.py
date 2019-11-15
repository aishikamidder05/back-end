

from. django.urls import path, include

def index(request):
    return HttpResponse('Hello user')

urlpatterns =
[

    path('', include('mysite.urls')),
]
