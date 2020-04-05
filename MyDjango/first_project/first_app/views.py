from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, Topic, Accessrecord
from . import forms
# Create your views here.

def index(request):
    
    webpages_list = Accessrecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list,'text':'hello world','number':100,'title':'HomePage'}
    return render(request, 'first_app/index.html',context=date_dict)

#relative urls view
def relative(request):
    myRel = {'rella':"Say my Name to Relative URLSs...!",'title':'RELATIVE PAGE'}
    return render(request,'first_app/relative_url.html',context=myRel)

def form_view_name(request):
    form = forms.FormName()#creating a new instance of the formName we created in forms.py and store it in form now called
    
    if request.method == "POST":
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            #do something
            print("Validation success! ")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
    
    return render(request, "first_app/form_page.html", {'myform':form})
    