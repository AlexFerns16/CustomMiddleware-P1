from django.urls import path, include
from blog import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('excp/', views.exception, name='excp'),
    path('userinfo/', views.userinfo, name='userinfo'),
]
