from django.urls import path

from login import views

urlpatterns = [
    path('', views.login1, name='login1'),
    path('register/', views.register, name='register'),
    path('guest/', views.guest, name='guest'),
    path('register_user/', views.register_user, name='register_user'),
    path('profile/',views.profile,name='profile'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('controls/',views.controls,name='controls'),
    path('alarma/',views.alarma,name='alarma'),
    path('alarma_user/',views.alarma_user,name='alarma_user'),
]