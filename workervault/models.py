from django.db import models

# Create your models here.

class WorkerVaultModel(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(default = "", max_length = 50)
    phoneno = models.IntegerField(default = "")
    emailid = models.EmailField(default = "", max_length = 50)
    address = models.CharField(default = "", max_length = 100)
    gender = models.CharField(default = "", max_length = 20)
    location = models.CharField(default = "", max_length = 50)
    password = models.CharField(default = "", max_length = 30)