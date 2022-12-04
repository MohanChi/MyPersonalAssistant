from django.db import models

# Create your models here.

class task_Model(models.Model):
       id = models.AutoField(primary_key=True)
       taskname =models.CharField(max_length=32)
       due = models.DateTimeField()
       priority = models.CharField(max_length=32)
       type = models.CharField(max_length=32)
       difficulty = models.CharField(max_length=32)
       detail = models.CharField(max_length=32)
       visible = models.CharField(max_length=32)

class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)