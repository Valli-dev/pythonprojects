from django.db import models
from datetime import datetime

class Student(models.Model):
    
    first_name = models.CharField(max_length =50)
    last_name= models.CharField(max_length =50)
    age= models.IntegerField()
    department = models.CharField(max_length =50)
    date_of_resumption = models.DateField(default =datetime.today)


