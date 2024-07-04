from django.contrib import admin

from django.contrib import admin
from .models import Project, Module, TaskProgress

admin.site.register(Project)
admin.site.register(Module)
admin.site.register(TaskProgress)

