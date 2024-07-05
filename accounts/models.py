
# from django.db import models
# from django.contrib.auth.models import User

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
#     contributors = models.ManyToManyField(User, related_name='contributing_projects', blank=True)

#     def __str__(self):
#         return self.name

# class Module(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='modules')
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     estimated_time = models.PositiveIntegerField()  # Estimated time in hours
#     actual_time = models.PositiveIntegerField(default=0)  # Time spent in hours

#     def __str__(self):
#         return self.name

# class TaskProgress(models.Model):
#     module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='progress')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     time_spent = models.PositiveIntegerField()  # Time spent in hours
#     date_logged = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.module.name} - {self.user.username} - {self.time_spent}h"

# models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_to_finish = models.IntegerField(help_text="Time to finish the project in days")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Segment(models.Model):
    project = models.ForeignKey(Project, related_name='segments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_to_finish = models.IntegerField(help_text="Time to finish the segment in days")

    def __str__(self):
        return f"{self.project.name} - {self.name}"
