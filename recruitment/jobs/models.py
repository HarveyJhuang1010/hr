from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

JobTypes = [
    (0, "Technology"),
    (1, "Product"),
    (2, "Operation"),
    (3, "Design"),
]

Cities = [
    (0, "Taipei"),
    (1, "Tokyo"),
    (2, "New York"),
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="Job Type")
    job_name  = models.CharField(max_length=250, blank=False, verbose_name="Job Name")
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="City")
    job_responsibility= models.TextField(max_length=1024, blank=False, verbose_name="Job Responsibility")
    job_requirements = models.TextField(max_length=1024, blank=False, verbose_name="Job Requirements")
    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.SET_NULL, null=True, default="admin")
    created_at = models.DateTimeField(verbose_name="Created at", default=datetime.now)
    updated_at = models.DateTimeField(verbose_name="Updated at", default=datetime.now)
