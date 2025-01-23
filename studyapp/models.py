from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

class UsersStudy(models.Model):
    Phases = [
        ('Phase I','Phase I'),
        ('Phase II','Phase II'),
        ('Phase III','Phase III'),
        ('Phase IV','Phase IV'),
    ]
    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=255,choices=Phases)
    sponser_name = models.CharField(max_length=255)
    admin = models.ForeignKey(Register,on_delete=models.CASCADE)




# Create your models here.
