"""food2go URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

HANDLER400 = TemplateView.as_view(template_name='errors/400.html')
HANDLER403 = TemplateView.as_view(template_name='errors/403.html') #'main.views.custom_403_view'
HANDLER404 = TemplateView.as_view(template_name='errors/404.html') #'main.views.custom_404_view'
HANDLER500 = TemplateView.as_view(template_name='errors/500.html') #'main.views.custom_500_view'

urlpatterns = [
    #path('', include('main.urls'), name='main'),
    path('pizza2go/', include('pizza2go.urls'), name='pizza2go'),
    path('admin/', admin.site.urls),
    #link structure imported from library
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
