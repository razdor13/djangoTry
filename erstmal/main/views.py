from django.shortcuts import render


def index(request):
    data = {
        "title": "головна сторінка",
        'values' :['some','hello','123123']
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")
