from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    fav_number = models.IntegerField()
    this_user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)