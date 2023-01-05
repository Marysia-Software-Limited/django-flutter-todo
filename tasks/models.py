from django.db import models


class Task(models.Model):
    name = models.TextField(max_length=1024)
    is_done = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
