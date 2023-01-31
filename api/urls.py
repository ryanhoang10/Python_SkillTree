# Returns an element for inclusion in urlpatterns. 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.skillTreeList),
    path('skilltree/<int:pk>/', views.skillTreeDetails),
]