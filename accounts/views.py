from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('welcome')


# model stuff
from django.shortcuts import render, redirect
from .forms import ProjectForm, SegmentForm
from .models import Project
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            # Redirect to create_module view with project_id
            return redirect('create_segment', project_id=project.pk)
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})

# def create_segment(request):
#     project_id = request.session.get('project_id')
#     if not project_id:
#         return redirect('create_project')

#     project = Project.objects.get(id=project_id)
#     if request.method == 'POST':
#         form = SegmentForm(request.POST)
#         if form.is_valid():
#             segment = form.save(commit=False)
#             segment.project = project
#             segment.save()
#             if 'add_another' in request.POST:
#                 return redirect('create_segment')
#             else:
#                 del request.session['project_id']
#                 return redirect('project_detail', project_id=project.id)
#     else:
#         form = SegmentForm()

#     return render(request, 'create_module.html', {'form': form, 'project': project})
# from django.shortcuts import render, redirect, get_object_or_404
# def create_segment(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     if request.method == 'POST':
#         form = SegmentForm(request.POST)
#         if form.is_valid():
#             segment = form.save(commit=False)
#             segment.project = project
#             segment.save()
#             if 'add_another' in request.POST:
#                 return redirect('create_segment', project_id=project.id)
#             else:
#                 return redirect('project_detail', project_id=project.id)
#     else:
#         form = SegmentForm()

#     return render(request, 'create_segment.html', {'form': form, 'project': project})


# views.py
from django.urls import reverse

def some_view(request):
    project_id = 1  # example project_id
    return redirect(reverse('create_segment', kwargs={'project_id': project_id}))
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import SegmentForm

def create_segment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = SegmentForm(request.POST)
        if form.is_valid():
            segment = form.save(commit=False)
            segment.project = project
            segment.save()
            if 'add_another' in request.POST:
                return redirect('create_segment', project_id=project.id)
            else:
                return redirect('project_detail', project_id=project.id)
    else:
        form = SegmentForm()

    return render(request, 'accounts/create_segment.html', {'form': form, 'project': project})


from django.shortcuts import render, get_object_or_404
from .models import Project

# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     segments = project.segment_set.all()  # Assuming Segment model is related to Project with a ForeignKey
#     return render(request, 'accounts/project_detail.html', {'project': project, 'segments': segments})

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    segments = project.segment_set.all()  # This will retrieve all segments related to the project
    return render(request, 'accounts/project_detail.html', {'project': project, 'segments': segments})
