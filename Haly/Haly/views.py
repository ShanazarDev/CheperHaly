from django.shortcuts import render


def home(request):
    return render(request, 'ru/index.html')
