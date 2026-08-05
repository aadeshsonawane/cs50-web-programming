from django.urls import include, path   

from newyear import views
from newyear.views import index


urlpatterns = [
    path('', views.index, name='index'),   #default page
  
]