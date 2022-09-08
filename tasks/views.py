from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HTTPResponse('Hello World')

def tasklist(request):
    return render(request, 'task/list.html')


# Create your views here.
