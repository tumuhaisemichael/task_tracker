# from django.contrib import admin

# from django.contrib import admin
# from .models import Project, Module, TaskProgress

# admin.site.register(Project)
# admin.site.register(Module)
# admin.site.register(TaskProgress)

# admin.py
from django.contrib import admin
from .models import Project, Segment

# Register your models here.
admin.site.register(Project)
admin.site.register(Segment)