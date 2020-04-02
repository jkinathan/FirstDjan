from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^formspage',views.form_view_name,name='My form'),
]