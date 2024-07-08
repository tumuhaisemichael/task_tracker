# models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # time_to_finish = models.IntegerField(help_text="Time to finish the project in days")
    time_to_finish = models.IntegerField(null=True, blank=True)
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
