from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),    
    path('login.html', views.loginPage, name='login'),
    path('logout.html',views.logoutPage,name='logout'),
    path('register_user.html', views.registerUser, name = 'register_user'),
    path('create_report.html', views.createReport, name='create_report'),
    path('customer.html/<str:pk_test>', views.customer, name='customer'),
]