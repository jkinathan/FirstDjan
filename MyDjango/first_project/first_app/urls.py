from django.conf.urls import url
from first_app import views


#TEMPLATE TAGGING 
app_name = 'firstapp'
#so here i removed the app_name = 'firstapp' from this urls.py in first_app  please check the project urls.py for the change
#edited traditional path links to url links
urlpatterns = [
    #now we have to start calling the CBV class
    #like url(r'^$',views.CBView.as_view()),
    url(r'^sch$',views.CBView.as_view()),
    url(r'^formspage',views.form_view_name,name='Myform'),
    url(r'^relative/$', views.relative,name='relname'),#this is the page for testing relative paths in django
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^school/$',views.SchoolListView.as_view(),name='list'), #finally did the magic
    #some alien regular expressions hahaha
    url(r'^school/(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail')# passing in the primarykey related to the particular schools detail
    #this is how we roll
]