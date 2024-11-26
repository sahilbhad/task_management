from django.db import models
from django.contrib.auth.models import User
 

class Task(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    host_id=models.ForeignKey(User,on_delete=models.CASCADE)

class HistoryTask(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    host_id=models.ForeignKey(User,on_delete=models.CASCADE)



class completed(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    host_id=models.ForeignKey(User,on_delete=models.CASCADE)





class cont(models.Model):
     fname=models.CharField(max_length=20)
     lname=models.CharField(max_length=20)
     email=models.CharField(max_length=20)
     message=models.TextField(max_length=100)

 




# class Abc(models.Model):
#     name=models.CharField(max_length=20)
#     surname=models.CharField(max_length=100)
