from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=265)
    second_name = models.CharField(max_length=265)
    phone = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name, self.second_name