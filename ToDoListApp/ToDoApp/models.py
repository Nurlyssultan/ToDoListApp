from django.db import models

# Create your models here.
class ToDoClass(models.Model):
    content = models.CharField(max_length=20)
    def __str__(self):
        return self.content
