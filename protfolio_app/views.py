from django.shortcuts import render
from protfolio_app.models import Project
# Create your views here.
def protfolio(request):
    project = Project.objects.all()
    return render(request, "protfolio.html", {"project":project})
