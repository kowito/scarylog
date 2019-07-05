from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'website', 'bio', 'phone', 'city', 'country']