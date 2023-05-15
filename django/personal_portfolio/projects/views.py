from django.shortcuts import render
from projects.models import Project

def project_index(request):
    
    return render(request, 'projects/project_index.html', {'projects': Project.objects.all()})


def project_detail(request, pk):
    
    return render(request, 'projects/project_detail.html', {'projects': Project.objects.get(pk=pk)})