from django.http.request import HttpRequest
from django.shortcuts import render
from django.template.defaultfilters import register


@register.filter
def lower(value):
    return value.lower()


@register.filter
def sum(a, b):
    return a+b


def index(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        context = {"name": name, "password": pwd}
        return render(request, "index.html", context)
    return render(request, "index.html")
