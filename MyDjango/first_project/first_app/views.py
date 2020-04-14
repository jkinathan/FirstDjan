#FUNCTION BASED VIEWS
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, Topic, Accessrecord, School, Student
from . import forms
from . import models
from first_app.forms import UserForm, UserProfileInfoForm

#these are for the login now
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required # if u require a user to be logged in 

#class based view imports
from django.views.generic import View, TemplateView, ListView, DetailView
# Create your views here.

#a class based views

class SchoolListView(ListView):
    #but we can modify it this way
    context_object_name = 'schools'
    model = models.School
    #its returning a list with school_list with underscore
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'#as for detailview it just returns model name lowercase in this case school
    model = models.School
    template_name = 'first_app/schoolDetail.html'
    
class CBView(TemplateView): #which is inheriting from our imported View
    template_name = 'first_app/Mycbv.html'
    #now doing the returning dictionary
    
    def get_context_data(self, **kwargs): #take **kwargs keyword arguments and take them as a dictionary and for the *args its just for simple arguments and you are not specifying the number of arguments required in a function call
        context = super(TemplateView, self).get_context_data(**kwargs) #python 2.7 has issues mahn so we use --super(TemplateView, self)-- instead of super() just mehn am shifting to python 3 
        context['injectme'] = 'Basic Injection'#here is the real context you pass in the key and values
        return context
    
def index(request):
    
    webpages_list = Accessrecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list,'text':'hello world','number':100,'title':'HomePage'}
    return render(request, 'first_app/index.html',context=date_dict)

@login_required #to make sure the view below requires a login
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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
    
def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() #grab user form and save to the database
            user.set_password(user.password) #hashing the password in the db
            user.save() #then save
            
            profile = profile_form.save(commit=False)
            profile.user = user #this sets up the one to one relationship
            
            #checking if they provided a profile picture
            if 'profile_pic' in request.FILES: #checking if it exists can also do for csv files
                profile.profile_pic = request.FILES['profile_pic']#dictionary## key based on what u defined in the models
            
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
            
    else:
        user_form = UserForm() #else meaning its a GET method which will make u see the actual form through this instance
        profile_form = UserProfileInfoForm()
        
    return render (request,'first_app/register.html',
               {'registered':registered,'user_form':user_form,'profile_form':profile_form})#dope as way to pass in multiple contexts heheh been looking for this big time hahaha


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'first_app/login.html',{})
    
#getting on with Class based views