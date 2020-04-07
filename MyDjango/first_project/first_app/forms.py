from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
        
class UserProfileInfo(forms.ModelForm):
    class Meta():
        fields = ('portfolio_site','profile_pic')

#custom validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")
class FormName(forms.Form):
    name = forms.CharField()#validators=[check_for_z]
    email = forms.EmailField()
    verifyemail =forms.EmailField(label="Enter your Email again!!!")
    text = forms.CharField(widget = forms.Textarea)
    
