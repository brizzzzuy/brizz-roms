from django.shortcuts import render
from .models import Tweak


def tweak_list_view(request):
    tweaks = Tweak.objects.all()
    return render(request, 'tweaks/tweak_list.html', {'tweaks': tweaks})
