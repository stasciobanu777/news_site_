from django.shortcuts import render
from .models import Articles


def poster(request):
    ticket = Articles.objects.all
    return render(request, 'post/html/poster.html', {'ticket': ticket})
