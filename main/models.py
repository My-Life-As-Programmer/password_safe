from django.db import models
from django.utils import timezone

# Create your models here.

class Servers(models.Model):
    hostname = models.CharField(max_length=50, unique=True, primary_key=True)
    ip = models.CharField(max_length=15, unique=True)
    class Meta:
        verbose_name_plural ='Servers'
    def __str__(self):
        return self.hostname

class ServerDetails(models.Model):
    hostname =  models.ForeignKey(Servers, on_delete=models.CASCADE)
    password = models.CharField(max_length=50, default='hi')
    last_password = models.CharField(max_length=50, default='hi')
    last_password_modified = models.DateTimeField(default=timezone.now)

    #def __str__(self):
    #    return self.hostname

    class Meta:
        verbose_name_plural ='ServerDetails'

