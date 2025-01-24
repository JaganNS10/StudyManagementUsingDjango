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



