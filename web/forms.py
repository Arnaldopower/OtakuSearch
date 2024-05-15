from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CommentAnime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, label_suffix="")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, label_suffix="")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid login credentials.")
        return self.cleaned_data


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentAnime
        fields = ['body']


class RatingAnime:
    pass


class RatingForm(forms.ModelForm):
    class Meta:
        model = RatingAnime
        fields = ['rating']