from django.shortcuts import render
from .models import Project

def home(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/home.html', {'projects':projects})

def resume(request):
	return render(request, 'portfolio/resume.html')

def crossfit(request):
	return render(request, 'portfolio/crossfit.html')