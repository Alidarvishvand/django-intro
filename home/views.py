from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def sayhello(request):
    person = {'name': 'ali'}
    return render(request, 'hello.html',context=person)
def home(request):
    return render(request, 'home.html')