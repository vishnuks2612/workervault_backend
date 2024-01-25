from django.db import models

# Create your models here.

class WorkerVaultModel(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(default = "", max_length = 100)
    phoneno = models.BigIntegerField(null=True)
    emailid = models.EmailField(default = "", max_length = 254)
    address = models.CharField(default = "", max_length = 400)
    gender = models.CharField(default = "", max_length = 100)
    location = models.CharField(default = "", max_length = 100)
    password = models.CharField(default = "", max_length = 100)