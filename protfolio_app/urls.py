from django.urls import path
from protfolio_app import views

urlpatterns = [
    path("",views.protfolio,name="protfolio"),
]