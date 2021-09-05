from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from hcaptcha.fields import hCaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
class AccountUpdateForm(forms.Form):
    company_name = forms.CharField()
    address = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 8}), required = False)
    company_registration_number = forms.CharField()
    company_email = forms.EmailField()

class CreateNewUser(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())