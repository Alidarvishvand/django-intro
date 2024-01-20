from django.shortcuts import render
from django.http import HttpResponse 
from.models import Todo
# Create your views here.




def sayhello(request):
    person = {'name': 'ali'}
    return render(request, 'hello.html',context=person)
def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html',{'all':all})