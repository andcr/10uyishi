from django.shortcuts import render
from django.http import HttpResponse

def contents(requests):
    return HttpResponse('this is content page')