from django.shortcuts import render
from .models import  Profile


# Create your views here.
def profiles(request):
    prof = Profile.objects.all()
    context = {
        'profiles': prof
    }

    return render(request, 'users/index.html', context)


def user_profile(request, pk):

    return render(request, 'users/profile.html')
