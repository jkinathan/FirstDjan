"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from first_app import views
from django.conf.urls import include

app_name = 'firstapp' #here is where we included the app_name variable with the name we shall use to call in any of our templates
#for some reason it works perfectly probably a django version issue

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^first_app/',include('first_app.urls',namespace='firstapp')),#then i passed in the namespace='firstapp' here to my first_app urls so we can access it to the templates that need it
    url(r'^admin/', include(admin.site.urls)),
]
