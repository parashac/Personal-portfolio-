from django.urls import path
from protfolio_app import views

urlpatterns = [
    path("",views.protfolio,name="protfolio"),
    path("project/",views.project_list, name="project-list"),
    path("project-create/", views.project_create, name="project-create"),
    path("project-update/<int:pk>/",views.project_update, name="project-update"),
    path("project-list/<int:pk>/", views.project_delete, name="project-delete")

]