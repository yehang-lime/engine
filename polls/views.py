from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

from .models import Hello


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def hello(request):
    hello = Hello('xxxx')
    str = json.dumps(hello, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
    print(str)
    return HttpResponse(str)


