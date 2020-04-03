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
    
    #python 3 explicitly
    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vemail = all_clean_data['verifyemail']
        
    #     if email != vemail:
    #         raise forms.ValidationError("Make sure both emails match")
    # botcatcher = forms.CharField(required=False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    # def clean_botcatcher(self):
    #     botcher = self.cleaned_data['botcatcher']
    #     if len(botcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcher