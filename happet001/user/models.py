from django.db import models

# Create your models here.

class User(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name




