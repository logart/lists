# coding=utf-8
from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Наименование товара")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Товар"


class Order(models.Model):
    item = models.ForeignKey(Item, blank=False, verbose_name=u"Товар")
    quantity = models.IntegerField(default=0, blank=False, verbose_name=u"Количество товара")
    executor = models.CharField(max_length=30, blank=False, verbose_name=u"Исполнитель")
    done = models.BooleanField(default=False, blank=False, verbose_name=u"Выполнено")