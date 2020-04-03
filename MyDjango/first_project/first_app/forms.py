from django import forms
from django.core import validators

#custom validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")
class FormName(forms.Form):
    name = forms.CharField()#validators=[check_for_z]
    email = forms.EmailField()
    verifyemail =forms.EmailField(label="Enter your Email again!!!")
    text = forms.CharField(widget = forms.Textarea)
    