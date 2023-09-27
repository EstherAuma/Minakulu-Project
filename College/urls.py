from django.urls import path
from College import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
    path('home/',views.home, name='home'),
    path('data_form',views.data_form, name='data_form'),
    path('lib',views.lib, name='lib'),
    
]

