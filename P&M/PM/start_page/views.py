from django.shortcuts import render


def index(request):
    return render(request, "start_page/start.html")