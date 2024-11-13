from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.index,name='index'),
    path('budget',views.budget,name='budget'),
    path('location',views.location,name='location'),
    path('Ts',views.Ts,name='Ts'),
    path('Tn',views.Tn,name='Tn'),
    path('success',views.success,name='success')
    
]