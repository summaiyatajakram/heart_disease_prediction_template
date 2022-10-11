from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index.html'),
    path('register/',views.register,name='register.html'),
    path('login/',views.login,name='login.html'),
]