from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if valid:
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if password != confirm_password or User.objects.filter(username=username).exists():
                valid = False
        return valid
