from django.urls import path
from . import views




urlpatterns = [
    path('main/', views.object_list, name='main'),
    path('register/', views.registerPage, name='register'),
	path('', views.loginPage, name='login'),  
	path('logout/', views.logoutUser, name="logout"),
    path('create/', views.createUser, name="create"),
    
    ]