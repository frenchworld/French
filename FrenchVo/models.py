from django.db import models

# Create your models here.
class French(models.Model):
    name= models.TextField(max_length=100)
    engname= models.TextField(max_length=100)

class Verbir(models.Model):
    irname = models.TextField(max_length=100)
    irengname = models.TextField(max_length=100)

class Verber(models.Model):
    ername= models.TextField(max_length=100)
    erengname= models.TextField(max_length=100)

class Verbre(models.Model):
    rename= models.TextField(max_length=100)
    reengname= models.TextField(max_length=100)