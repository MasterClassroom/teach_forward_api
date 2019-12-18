from django.http import HttpResponse
from django.shortcuts import render
from models.models import models
from .serializers import UsersSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the intreped index.")
