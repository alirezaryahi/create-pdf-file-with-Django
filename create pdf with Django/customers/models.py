from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    description = models.TextField()
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
