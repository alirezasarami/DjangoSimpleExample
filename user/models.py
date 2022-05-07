from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Log(models.Model):
    user = models.ForeignKey(User , on_delete=models.DO_NOTHING , related_name='log')
    action = models.CharField(max_length=200)
    tim = models.DateTimeField(auto_now_add=True) 
    ip = models.GenericIPAddressField( null=True)
    browser = models.CharField(max_length=255 , null=True)
    country = models.CharField(max_length=50 , null=True)

