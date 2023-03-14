from django.db import models

# Create your models here.
class Books(models.Model):
    bname= models.CharField(max_length=50, unique=True, default=False)
    bauthor= models.CharField(max_length=30, default=False)
    bdesc= models.TextField(default=False)
    blink= models.TextField()


