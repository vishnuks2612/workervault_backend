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
    
    
    
class AddNews(models.Model):
    newsid = models.AutoField(primary_key=True)
    title = models.CharField(default = "", max_length = 100)
    description = models.CharField(default = "", max_length = 250)
    image = models.CharField(default = "", max_length = 5000)
    location = models.CharField(default = "", max_length = 200)
    content = models.CharField(default = "", max_length = 500)
    
    
    
class AdminAdd(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(default = "", max_length = 100)