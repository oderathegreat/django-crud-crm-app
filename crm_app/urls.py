"""
URL configuration for crm_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'transactions', views.Transdata)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('client_record/<int:pk>', views.clientRecord, name='client-record'),
    path('delete_record/<int:pk>', views.deleteRecord, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('loginapi/', views.login_api, name='login-api'),

    path('test_transactions/', views.test_transactions, name='tests'),


    path('api/', include(router.urls)),


]
