from django.urls import include, path

from hello.views import aadesh, greet, index

urlpatterns = [
    path('', index, name='index'),   #default page
    path('aadesh/', aadesh, name='hello'), 
    path('<str:name>/', greet, name='greet'),
]