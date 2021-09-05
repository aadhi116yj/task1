from django.db import models

# Create your models here.

class students(models.Model):
    sname = models.CharField(max_length=50)
    sroll = models.IntegerField(max_length=50)
    sbranch = models.CharField(max_length=50)
    semail = models.EmailField(max_length=50)
    smobail = models.IntegerField()

    def __str__(self):
        return self.sname,self.sroll



    

