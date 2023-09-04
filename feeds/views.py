from django.shortcuts import render

from Adminside.models import PersonalInformation,About,Projects
from Adminside.models import *
# Create your views here.
def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    print(skills)
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills,
    }

    return render(request, 'feeds/home_page.html', context)