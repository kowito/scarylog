from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    # phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = UserProfile
        fields = ['gender', 'phone', 'bio']


class ProfilePictureForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('photo', )
