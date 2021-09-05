from django.db import models

# Create your models here.
class Register(models.Model):
    genders = [('Female','Female'),
               ('Male','Male')
    ]
    branches = [('Select','Select'),('CSE','CSE'),('MECH','MECH'),('CIVEL','CIVEL'),('ECE','ECE'),('EEE','EEE'),('IT','IT')]


    names = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=genders, null=True)
    branch = models.CharField(max_length=10, choices=branches, null=True)