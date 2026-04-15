from django.shortcuts import render
from .models import TeamMember


def home(request):
    return render(request, 'core/home.html')


def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'core/about.html', {'team_members': team_members})
