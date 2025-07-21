from django.shortcuts import render
from .models import Profile


# Create your views here.
def profiles(request):
    prof = Profile.objects.all()
    context = {
        'profiles': prof
    }

    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")
    other_skills = prof.skill_set.filter(description="")

    context = {
        'profile': prof,
        'top_skills': top_skills,
        "other_skills": other_skills
    }

    return render(request, 'users/profile.html', context)
