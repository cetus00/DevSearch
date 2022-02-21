from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    msg = 'You are on the projects page'
    return render(request, 'projects/projects.html', {'msg':msg})

def project(request, pk):
    return render(request, 'projects/single_project.html')