from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register ,name='register'),
    path('login/', views.user_login ,name='login'),
    path('profile/', views.profile ,name='profile'),
    path('logout/', views.user_logout ,name='logout'),
    path('user_changepass/', views.user_changepass ,name='user_changepass'),
    path('user_changepass2/', views.user_changepass2 ,name='user_changepass2'),
]
