from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=265)
    second_name = models.CharField(max_length=265)
    phone = models.IntegerField()
    age = models.IntegerField()
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'