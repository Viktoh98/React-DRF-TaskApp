from django.db import models
from django.conf import settings
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=50, unique=True)
    details = models.TextField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True,
                            blank=True, allow_unicode=True)

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
