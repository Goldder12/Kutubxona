from django.db import models

class Todo(models.Model):
    vaqt = models.DateField()
    malumot = models.CharField(max_length=50)
    faol = models.BooleanField()

    def __str__(self):
        return self.malumot
