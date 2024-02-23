from django.urls import path, include
from blog import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
