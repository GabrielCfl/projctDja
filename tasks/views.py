from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
def helloworld(request):
    return HTTPResponse('Hello World')

# Create your views here.
