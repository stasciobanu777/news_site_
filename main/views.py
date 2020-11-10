from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/html/index.html')


def ticket(request):
    return render(request, 'main/html/ticket.html')


def about(request):
    return render(request, 'main/html/about.html')


def contacts(request):
    return render(request, 'main/html/contacts.html')


def reviews(request):
    return render(request, 'main/html/reviews.html')
