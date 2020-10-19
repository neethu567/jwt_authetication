from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class student(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=20,blank=True)
    last_name=models.CharField(max_length=20,blank=True)

    class Meta:
        ordering=['first_name']

    def __str__(self):
        return "%s " % (self.first_name)