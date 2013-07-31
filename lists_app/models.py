from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, blank=False)
    quantity = models.IntegerField(default=0, blank=False)
    executor = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(default=False, blank=False)