from django.conf.urls import url
from first_app import views


#TEMPLATE TAGGING 

#so here i removed the app_name = 'firstapp' from this urls.py in first_app  please check the project urls.py for the change

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^formspage',views.form_view_name,name='Myform'),
    url(r'^relative/$', views.relative,name='relname'),#this is the page for testing relative paths in django
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
]