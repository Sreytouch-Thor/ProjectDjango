from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    path('create_order/', views.createOrder, name='createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='deleteOrder'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('user/', views.userPage, name='user_page'),
    path('account/', views.accountSettings, name='account'),

]