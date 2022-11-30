from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=80, null=False)
    birthdate = models.DateField(null=False)
    enter_year = models.IntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    