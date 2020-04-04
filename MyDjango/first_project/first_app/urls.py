from django.conf.urls import url
from first_app import views


#TEMPLATE TAGGING 


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^formspage',views.form_view_name,name='Myform'),
    url(r'^relative/$', views.relative,name='relname'),
]