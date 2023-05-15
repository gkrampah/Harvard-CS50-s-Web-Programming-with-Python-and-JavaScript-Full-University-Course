from django.shortcuts import render
from my_profile.models import About

def homepage(request):
    
    return render(request, 'my_profiles/data_index.html')


def about_view(request):
    abouts = About.objects.all()
    context = {
        "about": abouts,
    }
    return render(request, "my_profiles/about.html", context)

def publication_view(request):
    
    return render(request, 'my_profiles/publications.html')


