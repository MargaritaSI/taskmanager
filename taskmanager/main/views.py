from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.order_by('-id') #take all data from chart Task and send it to template
    return render(request, 'main/index.html', {'title': 'Main web page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    return render(request, 'main/create.html')