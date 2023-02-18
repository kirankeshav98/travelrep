from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Load(models.Model):
    neme=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    dis=models.TextField()

    def __str__(self):
        return self.neme

