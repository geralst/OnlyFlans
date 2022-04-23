"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from web.views import index,welcome,about,contacto,exito,colaboradores,register,exito_registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bienvenido', welcome, name='welcome'),
    path('acerca', about, name='about'),
    path('contacto',contacto,name='contacto'),
    path('exito',exito,name='exito'),
    path('colaboradores',colaboradores,name='colaboradores'),
    path('register',register,name='register'),
    path('exito_registro',exito_registro,name='exito_registro'),
    path('accounts/',include('django.contrib.auth.urls')),
]
