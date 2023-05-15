from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="index"),
    path("about/", views.about_view, name="about_index"),
    path("publications/", views.publication_view, name="publications_index"),
    
]