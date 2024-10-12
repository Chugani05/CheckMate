from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=1500)
    slug = models.SlugField(unique=True, max_length=100)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    check_box = models.BooleanField(default=False)

    def __str__(self):
        return self.title
