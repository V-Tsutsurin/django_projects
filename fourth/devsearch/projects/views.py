from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm

# Create your views here.
def projects(request):
    pr = Project.objects.all()

    context = {
        'projects': pr
    }

    return render(request, "projects/projects.html", context)

def project(request, pk):
    project_obj = Project.objects.get(id=pk)

    return render(request, 'projects/single-project.html', {'project': project_obj})


def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/form-template.html', context)
