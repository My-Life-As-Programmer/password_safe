from django.contrib import admin
from .models import Servers,ServerDetails

# Register your models here.
#class ServReg(Servers):

admin.site.register(Servers)
admin.site.register(ServerDetails)