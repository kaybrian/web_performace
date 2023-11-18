from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    # Your existing view logic here

    return render(request, 'index.html')
