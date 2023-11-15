from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Created By")
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    completed = models.BooleanField(default=False, verbose_name="Completed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title