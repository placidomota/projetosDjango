from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Alura space</h1><p>Ola alura</p>')

