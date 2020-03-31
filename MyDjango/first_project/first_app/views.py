from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    myDict = {'insert_me':"Now i am from from first_app/index.html"}
    return render(request, 'first_app/index.html',context=myDict)