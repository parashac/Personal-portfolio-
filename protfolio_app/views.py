from django.shortcuts import render, redirect
from protfolio_app.models import Project
from protfolio_app.forms import ProjectForm
# Create your views here.
def protfolio(request):
    projects = Project.objects.all()
    return render(request, "project_list.html", {"projects":projects})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_create(request):
    if request.method == "GET":
        form = ProjectForm()
        return render(request, "project_create.html", {"form": form})
    else:
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("project-list")

def project_update(request, pk):
    project = Project.objects.get(pk=pk)
    form= ProjectForm(request.POST, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project-list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})



def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return redirect("project-list")