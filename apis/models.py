from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
