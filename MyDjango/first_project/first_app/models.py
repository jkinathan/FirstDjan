from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=254)
    principal = models.CharField(max_length=24)
    location = models.CharField(max_length=245)
    #a string representation of that model incase we want to print it out
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        #tell it what primary key this school should be created with ... so we import reverse from url resolvers
        return reverse('firstapp:detail',kwargs={'pk':self.pk})
    

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name="students", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
    
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique=True)
    
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=265, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name

class Accessrecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)