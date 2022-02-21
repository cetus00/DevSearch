from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': "Fully functional ecommerce website"
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': "Project where I built my own portfolio"
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': "Opensource project I'm still working on"
    },
]


def projects(request):
    msg = 'projects'
    number = 11
    context = {'mag': msg, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single_project.html', {'project':projectObj})
