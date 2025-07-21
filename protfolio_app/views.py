from django.shortcuts import render
from protfolio_app.models import Project
# Create your views here.
def protfolio(request):
    projects = Project.objects.all()
    return render(request, "project_list.html", {"projects":projects})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})