# Returns an element for inclusion in urlpatterns. 
from django.urls import path
from . import views

urlpatterns = [
    path('skilltrees', views.skillsTreeList),
    path('skilltree/<int:pk>/', views.skillTreeDetails),
    path('users', views.usersList),
    path('user/<int:pk>/', views.userDetails),
    path('comment/<int:pk>/', views.commentDetails),
]