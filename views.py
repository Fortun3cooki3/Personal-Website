from django.shortcuts import render
from django.shortcuts import redirect
from .models import Projects, Cv, CoverLetter, Refrences, Webinfo 

def home_page(request):
        """homepage view"""
        coverletter = CoverLetter.objects.get()
        webinfo = Webinfo.objects.get()
        return render(request, "blog/homepage.html",{
                "coverletter": coverletter,
                "webinfo" : webinfo
        })


def projects(request):
        """project view to show all projects working/worked on"""
        projects = Projects.objects.all()
        coverletter = CoverLetter.objects.get()
        return render(request, "blog/projects.html", {
                "projects": projects,
                "coverletter": coverletter
        })

def project (request, slug):
        """project view to show a single project after the projects view"""
        project = Projects.objects.get(slug=slug)
        coverletter = CoverLetter.objects.get()
        return render(request, "blog/project.html",{
                "title": project.title,
                "description": project.description,
                "full_description": project.full_description,
                "git_hub": project.git_hub,
                "url": project.url,
                "image": project.image,
                "coverletter": coverletter
        })

def work_experience(request):
        """cv view, work experience, education and skills"""
        cv = Cv.objects.all().order_by('-start_date')
        coverletter = CoverLetter.objects.get()

        return render(request, "blog/cv.html", {
                "cv": cv,
                "coverletter": coverletter
        })

def refrences(request):
        refrences = Refrences.objects.all()
        coverletter = CoverLetter.objects.get()
        return render(request, "blog/refrences.html", {
                "refrences": refrences,
                "coverletter": coverletter

        })