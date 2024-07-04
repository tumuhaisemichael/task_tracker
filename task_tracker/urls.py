"""
URL configuration for task_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),  # For built-in auth views
    path('', accounts_views.home, name='home'),
    path('welcome/', accounts_views.welcome, name='welcome'),  # Add this line for the welcome page
    path('logout/', accounts_views.user_logout, name='logout'),
        # URL for creating a new project
    path('create_project/', accounts_views.create_project, name='create_project'),

    # URL for creating a new module
    # path('create_module/', accounts_views.create_module, name='create_module'),
    path('create_module/<int:project_id>/', accounts_views.create_module, name='create_module'),


]
