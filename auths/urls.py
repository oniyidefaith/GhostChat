from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('link', views.link_view, name='link'),
    path('room/<str:room_name>/', views.room_view, name='room'),
]
