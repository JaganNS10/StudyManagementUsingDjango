what is package and module?

PACKAGE: package is a directory contains one or more modules.
we can identify package by seeing there is any __init__.py

MODULE: Module is single file which contains classes,objects,functions and runnable code

PACKAGES AND MODULES USED IN THIS PROJECT

from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django import forms


>>> from django.contrib import admin
>>> print(admin)
<module 'django.contrib.admin' from 'C:\\Users\\heman\\AppData\\Roaming\\Python\\Python312\\site-packages\\django\\contrib\\admin\\__init__.py'>     


>>> import django.urls
>>> print(dir(django.urls))

>>>import inspect
>>>from django.contrib import admin
>>>print(inspect.getfile(admin)) It will gives the path
>>>print(inspect.getsource(admin)) It will gives the source code

models.py

from django.db import models

here django is a package and db is a subpackage.models is module which contains classes 
and functions

1:class ClassName(models.Model) models.Model.here models is a module and Model is a class

And then inside the parenthesis we are usisng models.Model that means we are inheriting the 
parent class from models module.
ClassName() is child class and Model() is a parent class

2:first_name = models.CharField(max_length=255) Here CharField() is a class inside the models 
module or file. we are creating object for the class CharField()

for example : 
class ClassName(args):
     //body of the program
Object = ClassName(args=255)

class CharField(max_length):
    //body of the program

first_name = CharField(max_length=255)

admin = models.ForeignKey(Register,on_delete=models.CASCADE) admin == Many and Register == One
ForeignKey-> It allows you to create a link between two database tables
Here ForeignKey is ManytoOneField that means the user can have many studies

Creating object

>>> from studyapp.models import Register,UsersStudy

>>> Object = Register(first_name='Hemanth',last_name='N.S',email='jagansenthilkumar@gmail.com',username='hxmenth',password='ns123',confirm_password='ns123')
>>> Object
<Register: Register object (None)>
>>> Object.save()
>>> Object
<Register: Register object (3)>
>>> Object.first_name
>>> 'Hemanth'

>>> ObjectUser = UsersStudy(study_name='study 1',study_description='study 1 is sample study',study_phase='Phase I',sponser_name='sponser 1',admin=Object)
>>> ObjectUser
<UsersStudy: UsersStudy object (None)>
>>> ObjectUser.save()
>>> ObjectUser
<UsersStudy: UsersStudy object (6)>
>>> ObjectUser.admin
<Register: Register object (3)>
>>> ObjectUser.admin.first_name
'Hemanth'

#Update
>>> ObjectUser.study_name = 'study 2'
>>> ObjectUser.study_name
'study 2'






