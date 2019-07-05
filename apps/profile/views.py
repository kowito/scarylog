from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm, ProfilePictureForm


@login_required
def profile_update(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=user)

    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def update_profile_picture_form(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        profile_picture_form = ProfilePictureForm(
            request.POST, request.FILES, instance=profile)
        if profile_picture_form.is_valid():
            profile_picture_form.save()

    profile_form = UserProfileForm(instance=profile)
    user_form = UserForm(instance=user)
    return render(request,
                  'profile_update.html', {
                      'user_form': user_form,
                      'profile_form': profile_form,
                  })
