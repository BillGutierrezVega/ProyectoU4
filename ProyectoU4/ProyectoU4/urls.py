"""ProyectoU4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, logout_then_login

from login.views import Vistaindex
#from login.views import LoginView
from login.views import form_proyecto, registro

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('LoginView', LoginView.as_view(), name='LoginView'),
    path('', Vistaindex.as_view(), name='Vistaindex'),
    path('regis', form_proyecto, name='regis'),
    path('registroUsuario', registro, name='registroUsuario'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('nombre22/', LoginView.as_view() ,name="nombre22")
    path('logout/', logout_then_login, name='logout'),
]
