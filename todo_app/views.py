from django.shortcuts import render


def home(request):
    return render(request, "todo_app/index.html")


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
