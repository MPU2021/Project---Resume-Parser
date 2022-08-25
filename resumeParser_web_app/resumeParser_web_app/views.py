# To check views,i am adding some functions to test how my website looks:

from re import search
from turtle import onclick
from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'search.html')