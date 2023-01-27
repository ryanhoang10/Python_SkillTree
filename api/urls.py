# Returns an element for inclusion in urlpatterns. 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('test', views.testGetData),
]