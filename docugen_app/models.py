from django.db import models

# Create your models here.

class Proektant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name