from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    name=models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=200)
    loc = models.CharField(max_length=20)

    def __str__(self):
        return self.name